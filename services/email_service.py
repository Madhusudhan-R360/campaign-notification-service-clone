import asyncio


async def send_email(recipient: str):

    print(
        f"EMAIL SENT TO: {recipient}"
    )

    await asyncio.sleep(3)

    return True