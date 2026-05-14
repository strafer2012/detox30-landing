
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DETOX-30 | UPGRADE YOUR LIFE</title>
    <style>
        :root {
            --bg-dark: #0f172a;
            --accent-neon: #38bdf8;
            --accent-pink: #f472b6;
            --text-white: #f8fafc;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
        body { background-color: var(--bg-dark); color: var(--text-white); line-height: 1.5; overflow-x: hidden; }
        .container { padding: 25px; max-width: 600px; margin: 0 auto; }
        
        header { text-align: left; padding: 60px 0 40px; position: relative; }
        h1 { font-size: 2.8rem; font-weight: 900; line-height: 1; text-transform: uppercase; margin-bottom: 20px; background: linear-gradient(to right, var(--accent-neon), var(--accent-pink)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .hero-sub { font-size: 1.2rem; opacity: 0.8; margin-bottom: 40px; border-left: 2px solid var(--accent-neon); padding-left: 15px; }

        .btn {
            display: flex; align-items: center; justify-content: center;
            background: rgba(56, 189, 248, 0.1); border: 1px solid var(--accent-neon);
            color: var(--accent-neon); padding: 18px; border-radius: 12px;
            text-decoration: none; font-weight: bold; font-size: 1rem; text-transform: uppercase;
            letter-spacing: 1px; transition: 0.3s; margin-bottom: 20px;
        }
        .btn-filled { background: var(--accent-neon); color: var(--bg-dark); }
        .btn:active { background: var(--accent-neon); color: var(--bg-dark); }

        section { margin-bottom: 60px; }
        h2 { font-size: 1.8rem; margin-bottom: 25px; letter-spacing: -1px; }

        .glass-card {
            background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 24px;
        }
        .pain-list { list-style: none; }
        .pain-list li { margin-bottom: 15px; display: flex; align-items: center; font-size: 1.1rem; }
        .pain-list li::before { content: '×'; color: var(--accent-pink); font-weight: bold; margin-right: 15px; font-size: 1.5rem; }

        .feature { margin-bottom: 30px; }
        .feature h3 { color: var(--accent-neon); margin-bottom: 10px; text-transform: uppercase; font-size: 0.9rem; }

        .reviews-grid { display: grid; gap: 15px; }
        .rev { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 16px; font-size: 0.9rem; }
        .rev-name { color: var(--accent-pink); font-weight: bold; margin-top: 10px; display: block; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Detox 30 <br>Quest</h1>
            <p class="hero-sub">Хакни свою зависимость. Забери фокус обратно за 30 дней.</p>
            <a href="https://t.me/detox_30_bot" class="btn btn-filled">Начать апгрейд</a>
        </header>

        <section>
            <h2>System Errors</h2>
            <div class="glass-card">
                <ul class="pain-list">
                    <li>Бесконечный думскроллинг</li>
                    <li>Цифровая тревожность</li>
                    <li>Потеря контроля над временем</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>The Protocol</h2>
            <div class="feature">
                <h3>01 / Daily Missions</h3>
                <p>Короткие задания в боте, которые меняют нейронные связи.</p>
            </div>
            <div class="feature">
                <h3>02 / Buddy Match</h3>
                <p>Ты не один. Твой напарник видит твой прогресс, а ты — его.</p>
            </div>
            <a href="https://t.me/detox_30_bot" class="btn">Подключиться к боту</a>
            <div class="feature" style="margin-top: 30px;">
                <h3>03 / Rewards System</h3>
                <p>Баллы, ачивки и реальный результат в часах свободного времени.</p>
            </div>
        </section>

        <section>
            <h2>User Reports</h2>
            <div class="reviews-grid">
                <div class="rev">"Самый технологичный способ бросить телефон. Результат на 3-й день."<span class="rev-name">@nikita_dev</span></div>
                <div class="rev">"Бадди-система это гениально. Нельзя подвести человека."<span class="rev-name">@elena_design</span></div>
                <div class="rev">"Минус 40% экранного времени за первую неделю. Полёт нормальный."<span class="rev-name">@max_startup</span></div>
                <div class="rev">"Наконец-то выспался. Рекомендую всем, кто живет в гаджетах."<span class="rev-name">@artem_v</span></div>
                <div class="rev">"Крутой UI у бота и понятная логика. 5 звезд."<span class="rev-name">@julia_m</span></div>
            </div>
        </section>

        <footer style="padding: 60px 0; text-align: center;">
            <a href="https://t.me/detox_30_bot" class="btn btn-filled">Вступить в игру</a>
            <p style="opacity: 0.3; font-size: 0.7rem; margin-top: 30px;">V.4.3 BUILD - 2026</p>
        </footer>
    </div>
</body>
</html>
