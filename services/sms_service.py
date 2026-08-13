import asyncio


async def send_sms(recipient: str):

    print(
        f"SMS SENT TO: {recipient}"
    )

    await asyncio.sleep(3)

    return True