# ITICKET APP

__Сервис предназначен для управления онлайн-продажами билетов на мероприятия. Администраторы смогут добавлять и редактировать мероприятия, а пользователи – просматривать доступные события, заказывать билеты и управлять заказами. Проект разрабатывается с использованием Django REST Framework для backend и Nuxt.js для frontend.__

## Setup

```sh
touch .env
```

```sh

## backend

* python 3.12

## Backend Setup

```sh
cd backend

python -m venv venv

source venv/bin/activate # source venv\Script\activate (Windows)

pip install -r requirements.txt
```

## Backend Development Server

```sh
python manage.py migrate

python manage.py runserver
```

## Frontend

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

### Frontend Setup

Make sure to install the dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

### Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev
```

### Frontend production

Build the application for production:

```bash
# npm
npm run build
```

Locally preview production build:

```bash
# npm
npm run preview
```
