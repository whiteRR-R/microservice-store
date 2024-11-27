def transactional(func):
    async def wrapper(self, *args, **kwargs):
        async with self.uow:
            try:
                result = await func(self, *args, **kwargs)
                await self.commit()
                return result
            except Exception as e:
                await self.uow.rollback()
                raise e
    return wrapper
