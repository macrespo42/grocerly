# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Grocerly is a Django REST Framework backend API for managing family grocery lists. Authentication uses JWT (SimpleJWT). Package management uses `uv`.

## Common Commands

```bash
# Install dependencies
uv sync --group dev

# Run development server
python manage.py runserver

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Run all tests
python manage.py test

# Run tests for a single app
python manage.py test accounts
python manage.py test groceries

# Lint and format
ruff check .
ruff format .
```

## Architecture

Two Django apps under the root directory:

- **`accounts/`** — Custom `User` model (extends `AbstractUser`) and `Family` model. Handles registration and JWT auth.
- **`groceries/`** — `Ingredient` catalog and `Grocery` (list items) models. Full CRUD via DRF ViewSets.
- **`config/`** — Django settings, main `urls.py`, wsgi/asgi entry points.

### Key relationships
- `User` → `Family` (optional FK; users may or may not belong to a family)
- `Grocery` → `Ingredient` (FK) and `Grocery` → `Family` (FK)

### Authentication flow
1. Register: `POST /accounts/register/`
2. Obtain token: `POST /api/token/` → returns `access` and `refresh` JWT tokens
3. Authenticated requests use `Authorization: Bearer <access>` header

### API structure
- `/accounts/` — auth routes (register)
- `/api/token/`, `/api/token/refresh/` — JWT endpoints
- `/api/ingredient/` — `IngredientViewSet` (full CRUD, unauthenticated)
- `/api/grocery/` — `GroceryView` (list + create, requires authentication)

## Settings

- **Settings module:** `config/settings.py`
- **Custom user model:** `accounts.User` (set as `AUTH_USER_MODEL`)
- **Default auth backend:** `JWTAuthentication` from SimpleJWT
- **Database:** SQLite3 (`db.sqlite3`) in development
- **Timezone:** `Europe/Paris`
