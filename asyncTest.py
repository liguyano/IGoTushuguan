import asyncio

async def foo():
    print("Foo is starting")
    await asyncio.sleep(2)  # Simulate an asynchronous operation
    print("Foo is done")

async def bar():
    print("Bar is starting")
    await asyncio.sleep(1)  # Simulate another asynchronous operation
    print("Bar is done")

async def main():
    await asyncio.gather(foo(), bar())  # Run both foo() and bar() concurrently

asyncio.run(main())  # Run the main asynchronous function
