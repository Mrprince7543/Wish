from flask import Flask, render_template_string

app = Flask(__name__)

# REHAN LOVES ZOE - THE 100-PAGE ULTRA-HD DARK EDITION
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>100 Pages of Love - Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; -webkit-tap-highlight-color: transparent; }
        
        body {
            background: #000;
            background: radial-gradient(circle at center, #1a0508 0%, #000000 100%);
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Ensures top/bottom boxes stay apart */
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            padding: 20px 10px;
        }

        /* HD Background Animations */
        .particle {
            position: absolute;
            pointer-events: none;
            animation: moveUp 6s linear forwards;
            z-index: 1;
            will-change: transform, opacity;
        }
        @keyframes moveUp {
            0% { transform: translateY(110vh) scale(0.3); opacity: 0; }
            50% { opacity: 0.7; }
            100% { transform: translateY(-20vh) scale(1.2); opacity: 0; }
        }

        /* Top Section */
        .top-container { width: 100%; text-align: center; z-index: 20; }
        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.5rem;
            color: #ff4d6d;
            margin-bottom: 10px;
            text-shadow: 0 0 15px #ff4d6d;
        }
        .header-box {
            background: rgba(255, 77, 109, 0.15);
            backdrop-filter: blur(10px);
            border: 2px solid #ff4d6d;
            padding: 12px 40px;
            border-radius: 50px;
            display: inline-block;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.4);
        }
        .header-box h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.4rem;
            color: #fff;
            letter-spacing: 5px;
            text-transform: uppercase;
        }

        /* MAIN CARD - FIXED BLURRY ISSUE */
        .love-card {
            position: relative;
            width: 100%;
            max-width: 500px;
            height: 420px;
            border-radius: 30px;
            z-index: 5;
            border: 4px solid #fff;
            box-shadow: 0 0 50px rgba(255, 77, 109, 0.5);
            /* High Quality Background Settings */
            background-image: url('https://i.ibb.co/1YTf7R36/FB-IMG-16249452197243361.jpg');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover; /* Use cover for better scaling */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.55); /* Sharp text contrast */
            backdrop-filter: blur(1px); /* Reduced blur to keep image visible */
            z-index: 1;
        }

        .content-inner { position: relative; z-index: 2; width: 90%; text-align: center; }
        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 4rem;
            color: #ff4d6d;
            margin-bottom: 10px;
            text-shadow: 0 0 20px rgba(255, 77, 109, 0.8);
        }
        .typing-text {
            font-size: 1.5rem;
            color: #fff;
            font-weight: 700;
            min-height: 100px;
            line-height: 1.4;
        }

        /* Bottom Section */
        .bottom-container { width: 100%; text-align: center; z-index: 20; }
        .footer-box {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 15px 40px;
            border-radius: 60px;
            border: 2px solid #ff4d6d;
            display: inline-block;
            box-shadow: 0 0 25px rgba(255, 77, 109, 0.4);
        }
        .footer-box p { font-weight: 800; color: #fff; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 2px; }

        .btn {
            background: #ff4d6d;
            color: #fff;
            border: none;
            padding: 14px 35px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 15px;
            box-shadow: 0 0 15px #ff4d6d;
            transition: 0.3s;
        }
        .btn:hover { transform: scale(1.1); }

        #cursor {
            position: fixed;
            width: 25px; height: 25px;
            background: #ff4d6d;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
        }

        .screen { display: none; width: 100%; }
        .active { display: block; }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop preload="auto">
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="top-container">
        <div class="top-title">Happy Valentine's Day Zoe 😘</div>
        <div class="header-box"><h2>REHAN LOVES ZOE</h2></div>
    </div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        <div class="content-inner">
            <div id="page1" class="screen active">
                <h1>Hi Zoe ❤️</h1>
                <p class="typing-text" id="type1">Zoe, aaj hamari 100 pages ki dastan shuru hoti hai... Dil thaam kar baithiye.</p>
                <button class="btn" onclick="startApp()">SHURU KAREIN? ✨</button>
            </div>
            
            <div id="dynamic-content" class="screen">
                <h1 id="dyn-h1"></h1>
                <p class="typing-text" id="dyn-p"></p>
                <button class="btn" id="dyn-btn" onclick="nextStep()">AAGE DEKHO 🌹</button>
            </div>
            
            <div id="final-page" class="screen">
                <h1>Will You?</h1>
                <p class="typing-text">Zoe Verma, 100 panno ki is mohabbat ke baad... Kya aap hamesha mere saath rahoge? ❤️</p>
                <div style="display:flex; justify-content:center; gap:20px;">
                    <button class="btn" onclick="sayYes()">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#333;" onmouseover="moveNoButton()">NO</button>
                </div>
            </div>
        </div>
    </div>

    <div class="bottom-container">
        <div class="footer-box"><p>💖 I LOVE YOU MERI JAAN ZOE VERMA 💖</p></div>
    </div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');
        let currentPage = 0;

        const story = [
            { h: "01/100", p: "Aapki ek muskurahat mere bure se bure din ko haseen bana deti hai." },
            { h: "05/100", p: "Zindagi mein sab kuch mil gaya, jab se aap mile ho." },
            { h: "10/100", p: "Aapka mera khayal rakhna, meri har choti baat samajhna... Love it." },
            { h: "15/100", p: "Zoe, aap meri pehli aur aakhri khwahish ho." },
            { h: "20/100", p: "Maine kabhi nahi socha tha ki koi itna pyara bhi ho sakta hai." },
            { h: "25/100", p: "Aapki aankhon mein mujhe apni puri duniya dikhti hai." },
            { h: "30/100", p: "Wada hai mera, main kabhi aapka sath nahi chhodunga." },
            { h: "35/100", p: "Har pal, har saans mein bas aapka hi naam hai." },
            { h: "40/100", p: "Aap meri rani ho, aur main hamesha aapka bodyguard rahunga." },
            { h: "45/100", p: "Log kehte hain pyar ek baar hota hai, par mujhe aapse har roz hota hai." },
            { h: "50/100", p: "Adha safar tay kar liya, par hamara pyar anant hai." },
            { h: "55/100", p: "Aap jaisa koi nahi hai is puri kainaat mein." },
            { h: "60/100", p: "Har dua mein maine sirf aapki khushi maangi hai." },
            { h: "65/100", p: "Zoe, aap meri inspiration ho, meri takat ho." },
            { h: "70/100", p: "Mera har kal aapke bina adhura hai." },
            { h: "75/100", p: "Hum dono ki jodi duniya ki sabse best jodi hai." },
            { h: "80/100", p: "Aapki mithaas ne meri zindagi me shahad ghol diya hai." },
            { h: "85/100", p: "Zoe Verma, aap mere dil ki dharkan ho." },
            { h: "90/100", p: "Bas kuch hi kadam aur, aur hamari dastan amar ho jayegi." },
            { h: "95/100", p: "Zindagi bhar aapka hath tham kar chalna chahta hoon." },
            { h: "99/100", p: "I Love You More Than Words Can Ever Express." },
            { h: "100/100", p: "Aap meri ho, aur sirf meri rahoge... Hamesha." }
        ];

        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        function typeEffect(element, text) {
            let i = 0;
            element.innerHTML = "";
            clearInterval(window.typingInterval);
            window.typingInterval = setInterval(() => {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                } else { clearInterval(window.typingInterval); }
            }, 30);
        }

        function startApp() {
            music.play().catch(() => { window.addEventListener('click', () => music.play(), {once: true}); });
            document.getElementById('page1').style.display = 'none';
            document.getElementById('dynamic-content').style.display = 'block';
            nextStep();
        }

        function nextStep() {
            if (currentPage < story.length) {
                const data = story[currentPage];
                document.getElementById('dyn-h1').innerText = data.h;
                typeEffect(document.getElementById('dyn-p'), data.p);
                currentPage++;
            } else {
                document.getElementById('dynamic-content').style.display = 'none';
                document.getElementById('final-page').style.display = 'block';
            }
        }

        function sayYes() {
            alert('I Love You Tooo Much, Zoe Jaan! 😘😘😘');
            setInterval(() => createParticle('❤️'), 100);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

        function createParticle(symbol) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.innerHTML = symbol;
            p.style.left = Math.random() * 100 + 'vw';
            p.style.fontSize = (Math.random() * 20 + 10) + 'px';
            p.style.color = symbol === '❤️' ? '#ff4d6d' : '#fff';
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 6000);
        }

        setInterval(() => { createParticle('❤️'); createParticle('○'); }, 400);
        typeEffect(document.getElementById('type1'), "Zoe, aaj hamari 100 pages ki dastan shuru hoti hai... Dil thaam kar baithiye.");
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
