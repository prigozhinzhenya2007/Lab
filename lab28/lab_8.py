import aiohttp
import asyncio
import csv

URLS = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://www.python.org",
    "https://badurl.test",
    "https://httpbin.org/delay/5"
]

MAX_CONCURRENT_REQUESTS = 2
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

async def fetch(session, url, max_retries=3, delay=1):
    timeout = aiohttp.ClientTimeout(total=3)

    for attempt in range(1, max_retries + 1):
        async with semaphore:
            try:
                async with session.get(url, timeout=timeout) as response:
                    text = await response.text()
                    return {
                        "url": url,
                        "status": response.status,
                        "length": len(text),
                        "error": ""
                    }

            except asyncio.TimeoutError:
                error_msg = "Таймаут (ресурс долго не отвечает)"
            except aiohttp.ClientConnectorError:
                error_msg = "Ошибка соединения (ресурс недоступен)"
            except aiohttp.ClientError as e:
                error_msg = f"Сетевая ошибка: {e}"
            except Exception as e:
                error_msg = f"Неизвестная ошибка: {e}"

        if attempt < max_retries:
            print(f"[Попытка {attempt}/{max_retries}] Ошибка {url}. Повтор через {delay} сек...")
            await asyncio.sleep(delay)
            delay *= 2

    return {
        "url": url,
        "status": "FAIL",
        "length": 0,
        "error": error_msg
    }


async def main():
    print("Начинаем асинхронную загрузку данных...\n")

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        results = await asyncio.gather(*tasks)

    print("\n" + "=" * 105)
    print(f"| {'URL':<30} | {'Статус':<8} | {'Размер (байт)':<15} | {'Ошибки / Примечания':<40} |")
    print("=" * 105)
    for res in results:
        error_text = res['error'] if res['error'] else "Нет"
        print(f"| {res['url'][:30]:<30} | {str(res['status']):<8} | {str(res['length']):<15} | {error_text[:40]:<40} |")
    print("=" * 105)

    csv_filename = "lab8_results.csv"
    with open(csv_filename, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["url", "status", "length", "error"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\nДанные успешно сохранены в файл: {csv_filename}")

if __name__ == "__main__":
    asyncio.run(main())
