from typing import Generic, TypeVar

from beanie import Document, SortDirection
from loguru import logger
from pydantic import BaseModel
from pymongo.errors import DuplicateKeyError

T = TypeVar("T", bound=Document)


class BaseRepository(Generic[T]):
    """Base repository class for other repositories to inherit application.

    Args:
    ----
        Generic (_type_): _description_

    """

    def __init__(self: "BaseRepository[T]", model: T) -> None:
        """To initialize the BaseRepository with the given model.

        Args:
        ----
            model (T): _description_

        """
        self.model = model

    async def create(self: "BaseRepository[T]", document: BaseModel) -> T | None:
        """Create a document in the database.

        Args:
        ----
            document (BaseModel): _description_

        Returns:
        -------
            T | None: _description_

        """
        try:
            logger.info(f"Creating document: {document}")
            return await self.model(**document.model_dump()).insert()
        except DuplicateKeyError as e:
            logger.error(f"DuplicateKeyError: {e.details}")
            return None

    async def get(self: "BaseRepository[T]", document_id: str) -> T | None:
        """Get a document from the database.

        Args:
        ----
            document_id (str): _description_

        Returns:
        -------
            T | None: _description_

        """
        return await self.model.get(document_id)

    async def get_all(self: "BaseRepository[T]") -> list[T]:
        """Get all documents from the database.

        Returns
        -------
            list[T]: _description_

        """
        return await self.model.find_all().to_list()

    async def update(
        self: "BaseRepository[T]", document_id: str, document: BaseModel
    ) -> T | None:
        """Update a document in the database.

        Args:
        ----
            document_id (str): _description_
            document (BaseModel): _description_

        Returns:
        -------
            T | None: _description_

        """
        db_item = await self.get(document_id)
        if db_item:
            await db_item.update({"$set": document.model_dump(exclude_unset=True)})
            return db_item
        return None

    async def delete(self: "BaseRepository[T]", document_id: str) -> bool:
        """Delete a document from the database.

        Args:
        ----
            document_id (str): _description_

        Returns:
        -------
            bool: _description_

        """
        db_item = await self.get(document_id)
        if db_item:
            await db_item.delete()
            return True
        return False

    async def find(
        self: "BaseRepository[T]",
        criteria: dict,
        sort: str | list[tuple[str, SortDirection]] | None = None,
        limit: int | None = None,
    ) -> list[T]:
        """Find documents in the database.

        Args:
        ----
            criteria (dict): _description_
            sort (str | list[tuple[str, SortDirection]] | None, optional): _description_. Defaults to None.
            limit (int | None, optional): _description_. Defaults to None.

        Returns:
        -------
            list[T]: _description_

        """  # noqa: E501
        query = self.model.find(criteria)
        if sort:
            query = query.sort(sort)
        if limit:
            query = query.limit(limit)
        return await query.to_list()
