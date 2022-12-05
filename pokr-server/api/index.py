from fastapi import APIRouter

router = APIRouter()


@router.get("/health", description="서버 상태 확인", response_model=str)
def health_check() -> str:
    return "green"
