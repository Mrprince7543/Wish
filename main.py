from flask import Flask, render_template_string
import random

app = Flask(__name__)

# REHAN LOVES ZOE - MEGA 32-PAGE SMOOTH EDITION
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; -webkit-tap-highlight-color: transparent; }
        
        body {
            background: url('https://i.ibb.co/cSjzv48x/received-1191499147962097.jpg') center/cover no-repeat fixed;
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            padding: 10px;
            position: relative;
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 77, 109, 0.4);
            z-index: 1;
        }

        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.5rem;
            color: #fff;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 0 0 15px #ff0055, 0 0 30px #ff0055;
            z-index: 20;
            position: relative;
        }

        .header-box {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border: 2px solid #fff;
            padding: 10px 35px;
            border-radius: 50px;
            margin-bottom: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            z-index: 20;
            position: relative;
        }
        .header-box h2 { font-size: 1.3rem; color: #fff; letter-spacing: 3px; text-transform: uppercase; }

        /* MAIN CONTAINER */
        .love-card {
            position: relative;
            width: 100%;
            max-width: 550px;
            height: 450px;
            border-radius: 30px;
            z-index: 5;
            border: 5px solid #fff;
            box-shadow: 0 20px 50px rgba(0,0,0,0.4);
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            will-change: transform;
            position: relative;
        }

        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(3px);
            z-index: 1;
        }

        .content-inner { 
            position: relative; 
            z-index: 2; 
            width: 90%; 
            text-align: center; 
            padding: 20px;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #ffffff;
            margin-bottom: 15px;
            text-shadow: 2px 2px 20px #ff0055;
        }

        .typing-text {
            font-size: 1.5rem;
            color: #fff;
            font-weight: 700;
            min-height: 90px;
            text-shadow: 2px 2px 10px #000;
            line-height: 1.4;
            padding: 0 10px;
        }

        /* ATTRACTIVE FOOTER */
        .footer-box {
            margin-top: 20px;
            background: white;
            padding: 15px 40px;
            border-radius: 60px;
            border: 3px solid #ff4d6d;
            box-shadow: 0 5px 20px rgba(255, 77, 109, 0.5);
            z-index: 20;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .footer-box p { font-weight: 800; color: #ff4d6d; font-size: 1rem; text-transform: uppercase; margin: 0; letter-spacing: 1px;}

        .btn {
            background: #fff;
            color: #ff4d6d;
            border: none;
            padding: 15px 35px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transition: 0.3s;
            position: relative;
            z-index: 10;
        }
        .btn:hover { background: #ff4d6d; color: #fff; transform: scale(1.1); }

        #cursor {
            position: fixed;
            width: 20px; height: 20px;
            background: #fff;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            filter: drop-shadow(0 0 5px #ff4d6d);
        }

        .heart-float {
            position: absolute;
            color: #fff;
            pointer-events: none;
            animation: moveUp 5s linear forwards;
            z-index: 1;
        }
        @keyframes moveUp {
            0% { transform: translateY(110vh) scale(0.5); opacity: 0; }
            50% { opacity: 1; transform: translateY(50vh) scale(1); }
            100% { transform: translateY(-10vh) scale(0.5); opacity: 0; }
        }

        .screen { display: none; width: 100%; }
        .active { display: block; animation: fadeIn 0.5s; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        .page-counter {
            position: absolute;
            bottom: 10px;
            right: 15px;
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            z-index: 3;
        }
        
        .music-control {
            position: fixed;
            top: 15px;
            right: 15px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            cursor: pointer;
            z-index: 100;
            backdrop-filter: blur(5px);
            border: 2px solid white;
        }
        
        .music-control:hover {
            background: rgba(255, 255, 255, 0.3);
        }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <div class="music-control" onclick="toggleMusic()" id="musicBtn">🎵</div>
    
    <!-- Multiple music options for better compatibility -->
    <audio id="bgMusic" loop preload="auto" style="display:none;">
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>
    
    <audio id="bgMusic2" loop preload="auto" style="display:none;">
        <source src="https://assets.codepen.io/1468070/Happy+Valentine_s+Day+-+320bit.mp3" type="audio/mpeg">
    </audio>

    <div class="top-title">Happy Valentine's Day Zoe 😘</div>
    <div class="header-box"><h2>REHAN LOVES ZOE</h2></div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        <div class="content-inner">
            <div id="page1" class="screen active">
                <h1>Hi Jaan ❤️</h1>
                <p class="typing-text" id="type1">Zoe, aaj aapke liye 32 pages ka ek haseen safar shuru karte hain...</p>
                <button class="btn" onclick="startApp()">START JOURNEY ✨</button>
            </div>
            
            <div id="dynamic-content" class="screen">
                <h1 id="dyn-h1"></h1>
                <p class="typing-text" id="dyn-p"></p>
                <div class="page-counter" id="pageCounter"></div>
                <button class="btn" id="dyn-btn" onclick="nextStep()">AAGE DEKHO 🌹</button>
            </div>
            
            <div id="final-page" class="screen">
                <h1 style="font-size: 3rem;">Be Mine?</h1>
                <p class="typing-text">Zoe Verma, kya aap hamesha mere saath rahoge? Will you be mine forever? ❤️</p>
                <div style="display:flex; justify-content:center; gap:20px;">
                    <button class="btn" onclick="sayYes()">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#444; color:#fff;" onmouseover="moveNoButton()">NO</button>
                </div>
                <div class="page-counter">32/32</div>
            </div>
        </div>
    </div>

    <div class="footer-box"><p>💖 I LOVE YOU MERI JAAN ZOE VERMA 💖</p></div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');
        const music2 = document.getElementById('bgMusic2');
        let currentPage = 0;
        let isPlaying = false;
        let currentMusic = music;

        const story = [
            { h: "The Smile", p: "Aapki muskurahat dekh kar mera din ban jata hai, Miss Zoe." },
            { h: "Pure Soul", p: "Aapka dil itna saaf hai ki koi bhi aap se pyar kar baithe." },
            { h: "Dream Girl", p: "Maine sapno mein pari dekhi thi, asliyat mein aap mil gaye." },
            { h: "My Luck", p: "Main khud ko khush-naseeb samajhta hoon ki aap meri life mein ho." },
            { h: "Unique", p: "Duniya mein hazaaron hain, par 'Zoe' sirf ek hi hai." },
            { h: "Comfort", p: "Aap se baat karke aisa lagta hai jaise har tension khatam ho gayi." },
            { h: "Strength", p: "Jab aap mere saath hote ho, toh main kisi bhi mushkil se lad sakta hoon." },
            { h: "The Voice", p: "Aapki awaaz mere kaanon mein kisi music jaisa sukoon deti hai." },
            { h: "Eyes", p: "Aapki aankhon mein itni gehrai hai ki main kho jata hoon." },
            { h: "Style", p: "Aapka baat karne ka aur rehne ka andaaz ekdam alag aur pyara hai." },
            { h: "Thinking", p: "Main poore din bas ye sochta hoon ki aap kya kar rahe honge." },
            { h: "Trust", p: "Mujhe aap par poora bharosa hai, aap kabhi mera hath nahi chhodoge." },
            { h: "Special", p: "Zoe, aap mere liye mere family se kam nahi ho." },
            { h: "Laughter", p: "Aapka hansna mujhe duniya ki sabse badi khushi deta hai." },
            { h: "Admiration", p: "Main ghanton bas aapko dekh sakta hoon bina bore huye." },
            { h: "Presence", p: "Aapki maujoodgi se hi ghar aur dil dono bhare huye lagte hain." },
            { h: "Angel", p: "Bhagwan ne shayad aapko mere liye hi bheja hai." },
            { h: "Kindness", p: "Aapka doosron ki care karna mujhe bohot pasand hai." },
            { h: "Connection", p: "Humara rishta sirf baaton ka nahi, dil ka gehra rishta hai." },
            { h: "Memories", p: "Ab tak ki har ek minute jo maine aapke sath bitayi hai, wo precious hai." },
            { h: "Support", p: "Aapne mujhe tab samjha jab kisi ne nahi samjha." },
            { h: "Motivation", p: "Aapko dekh kar mujhe life mein behtar karne ki himmat milti hai." },
            { h: "Vibe", p: "Aapki energy itni positive hai ki sab positive lagne lagta hai." },
            { h: "Love", p: "Maine pyar ke baare mein suna tha, mehsoos aapke sath kiya." },
            { h: "Loyalty", p: "Rehan sirf Zoe ka hai, aur hamesha rahega." },
            { h: "Promise 1", p: "Wada hai, main aapko kabhi rone nahi doonga." },
            { h: "Promise 2", p: "Wada hai, main hamesha aapki har baat sununga." },
            { h: "Promise 3", p: "Wada hai, main har mushkil mein aapke aage khada rahunga." },
            { h: "Promise 4", p: "Wada hai, main hamesha aapka saath dunga har mausam mein." },
            { h: "Promise 5", p: "Wada hai, aapko kabhi akela nahi chhodunga." },
            { h: "Almost End", p: "Ab 32 pages ho chuke hain, par mera pyar abhi shuru hua hai." },
            { h: "The Queen", p: "Zoe Verma, aap mere dil ke takht ki akeli rani ho." }
        ];

        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        function playMusic() {
            if (!isPlaying) {
                // Try first music source
                currentMusic.play().then(() => {
                    isPlaying = true;
                    document.getElementById('musicBtn').innerHTML = '🔊';
                }).catch(() => {
                    // If first fails, try second source
                    currentMusic = music2;
                    currentMusic.play().then(() => {
                        isPlaying = true;
                        document.getElementById('musicBtn').innerHTML = '🔊';
                    }).catch(() => {
                        console.log("Music playback failed. User interaction may be required.");
                    });
                });
            }
        }

        function toggleMusic() {
            if (isPlaying) {
                currentMusic.pause();
                document.getElementById('musicBtn').innerHTML = '🔇';
            } else {
                playMusic();
            }
            isPlaying = !isPlaying;
        }

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
            // Try to play music when user interacts
            playMusic();
            
            document.getElementById('page1').style.display = 'none';
            document.getElementById('dynamic-content').style.display = 'block';
            nextStep();
        }

        function nextStep() {
            if (currentPage < story.length) {
                const data = story[currentPage];
                document.getElementById('dyn-h1').innerText = data.h;
                typeEffect(document.getElementById('dyn-p'), data.p);
                document.getElementById('pageCounter').innerText = `${currentPage + 1}/32`;
                currentPage++;
            } else {
                document.getElementById('dynamic-content').style.display = 'none';
                document.getElementById('final-page').style.display = 'block';
            }
        }

        function sayYes() {
            alert('I Love You Tooo Much, Zoe Jaan! 😘😘😘\nYou just made me the happiest person in the world!');
            setInterval(createHeart, 200);
            document.querySelector('.footer-box p').innerHTML = '💖 ZOE SAID YES! I LOVE YOU FOREVER! 💖';
            document.querySelector('.footer-box').style.background = '#ff4d6d';
            document.querySelector('.footer-box').style.color = '#fff';
            document.querySelector('.footer-box p').style.color = '#fff';
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
            btn.innerText = 'YES BHI BOLDO! 😘';
            btn.style.background = '#ff4d6d';
            btn.style.color = '#fff';
        }

        function createHeart() {
            if (document.querySelectorAll('.heart-float').length > 25) return;
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = (Math.random() * 20 + 20) + 'px';
            h.style.animationDuration = (Math.random() * 3 + 4) + 's';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 5000);
        }

        // Initialize
        typeEffect(document.getElementById('type1'), "Zoe, aaj aapke liye 32 pages ka ek haseen safar shuru karte hain...");
        setInterval(createHeart, 1000);
        
        // Auto-start music after a short delay (browsers may block this)
        setTimeout(() => {
            playMusic();
        }, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
