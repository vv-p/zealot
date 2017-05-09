from zealot.async import Suite

suite = Suite(threads=8)


@suite.register
async def test_one(session, semaphore):
    async with semaphore:
        async with session.get('https://api.github.com/events') as response:
            json = await response.json()
    assert len(json) == 30


@suite.register
async def test_two(session, semaphore):
    async with semaphore:
        async with session.get('https://api.github.com/events') as response:
            json = await response.json()
    assert len(json) == 29


suite.run()
