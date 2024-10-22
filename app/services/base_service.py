from typing import Generic, TypeVar

from beanie import SortDirection
from fastapi_pagination import paginate
from loguru import logger
from pydantic import BaseModel

from app.repositories.base_repo import BaseRepository

T = TypeVar("T", bound=BaseModel)
R = TypeVar("R", bound=BaseRepository)


class BaseService(Generic[T, R]):
    """Base service class for other services to inherit application."""

    def __init__(self: "BaseService[T, R]", repository: R) -> None:
        """To initialize the BaseService with the given repository.

        Args:
        ----
            repository (R): The repository instance to be used by the service.

        """
        self.repository = repository

    async def create(self: "BaseService[T, R]", data: T) -> T:
        """Create a document in the database."""
        logger.info(f"Creating document: {data}")
        return await self.repository.create(data)

    async def get(self: "BaseService[T, R]", document_id: str) -> T | None:
        """Get a document from the database."""
        return await self.repository.get(document_id)

    async def get_all(self: "BaseService[T, R]") -> list[T]:
        """Get all documents from the database."""
        return await self.repository.get_all()

    async def update(self: "BaseService[T, R]", document_id: str, data: T) -> T | None:
        """Update a document in the database."""
        return await self.repository.update(document_id, data)

    async def delete(self: "BaseService[T, R]", document_id: str) -> bool:
        """Delete a document from the database."""
        return await self.repository.delete(document_id)

    async def find(
        self: "BaseService[T, R]",
        criteria: dict,
        sort: str | list[tuple[str, SortDirection]] | None = None,
    ) -> list[T]:
        """Find documents in the database."""
        return await self.repository.find(criteria, sort=sort)

    async def find_paginated(
        self: "BaseService[T, R]",
        criteria: dict,
        page: int,
        page_size: int,
        sort: str | list[tuple[str, SortDirection]] | None = None,
    ) -> tuple[list[T], int]:
        """Find documents in the database and paginate the results.

        Args:
        ----
            criteria (dict): The criteria to filter the documents.
            page (int): The page number.
            page_size (int): The number of documents per page.
            sort (str | list[tuple[str, SortDirection]] | None): The sorting criteria.
                Defaults to None.

        Returns:
        -------
        tuple[list[T], int]: The paginated documents and the total number of documents.

        """
        return paginate(
            await self.repository.find(criteria, sort=sort), page, page_size
        )
