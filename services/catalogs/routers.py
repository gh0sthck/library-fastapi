from fastapi import APIRouter


catalog_router = APIRouter(prefix="/catalog", tags=["Catalog"])


@catalog_router.get("/all/")
async def get_all_catalogs() -> dict[str, int]:
    """Return all catalogs."""
    return {"test": 200}


@catalog_router.get("/{catalog_id}/")
async def get_id_catalog(catalog_id: int) -> dict[str, int]:
    """Return specific catalog by id."""
    return {"test": 200}
