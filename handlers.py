from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router
from weather import get_weather_data
from states import Form

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    await message.answer("Привет! Введите название города для получения прогноза погоды.")
    await state.set_state(Form.city)

@router.message(Form.city)
async def get_weather(message: types.Message, state: FSMContext):
    city = message.text
    weather_data = get_weather_data(city)
    if weather_data:
        await message.answer(
            f"Температура: {weather_data['main']['temp']}°C\n"
            f"Влажность: {weather_data['main']['humidity']}%\n"
            f"Описание: {weather_data['weather'][0]['description']}"
        )
    else:
        await message.answer("Город не найден. Пожалуйста, попробуйте еще раз.")
    await state.clear()
