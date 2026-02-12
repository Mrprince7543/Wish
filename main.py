from flask import Flask, render_template_string

app = Flask(__name__)

# REHAN LOVES ZOE - 50-PAGE MEGA SMOOTH EDITION
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>50 Pages of Love for Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; -webkit-tap-highlight-color: transparent; }
        
        body {
            background: #ff4d6d;
            background: linear-gradient(135deg, #ff0a54 0%, #ff758f 50%, #fecfef 100%);
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            padding: 10px;
        }

        /* Floating Bubbles & Hearts Background */
        .particle {
            position: absolute;
            pointer-events: none;
            animation: moveUp 6s linear forwards;
            z-index: 1;
            will-change: transform, opacity;
        }

        @keyframes moveUp {
            0% { transform: translateY(110vh) scale(0.5); opacity: 0; }
            10% { opacity: 0.8; }
            100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
        }

        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.5rem;
            color: #fff;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 0 0 15px #ff0055, 0 0 30px #ff0055;
            z-index: 20;
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
        }
        .header-box h2 { font-size: 1.3rem; color: #fff; letter-spacing: 3px; text-transform: uppercase; }

        .love-card {
            position: relative;
            width: 100%;
            max-width: 550px;
            height: 450px;
            border-radius: 30px;
            z-index: 5;
            border: 5px solid #fff;
            box-shadow: 0 20px 50px rgba(0,0,0,0.4);
            background: url('https://i.ibb.co/1YTf7R36/FB-IMG-16249452197243361.jpg') center/cover no-repeat;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(1.5px);
            z-index: 1;
        }

        .content-inner { position: relative; z-index: 2; width: 90%; text-align: center; }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 4rem;
            color: #ffffff;
            margin-bottom: 10px;
            text-shadow: 2px 2px 20px #ff0055;
        }

        .typing-text {
            font-size: 1.5rem;
            color: #fff;
            font-weight: 700;
            min-height: 100px;
            text-shadow: 2px 2px 10px #000;
            line-height: 1.4;
        }

        .footer-box {
            margin-top: 20px;
            background: white;
            padding: 15px 40px;
            border-radius: 60px;
            border: 3px solid #ff4d6d;
            box-shadow: 0 5px 20px rgba(255, 77, 109, 0.5);
            z-index: 20;
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
        }
        .btn:hover { background: #ff4d6d; color: #fff; transform: scale(1.1); }

        #cursor {
            position: fixed;
            width: 25px; height: 25px;
            background: #fff;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            filter: drop-shadow(0 0 5px #ff4d6d);
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

    <div class="top-title">Happy Valentine's Day Zoe 😘</div>
    <div class="header-box"><h2>REHAN LOVES ZOE</h2></div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        <div class="content-inner">
            <div id="page1" class="screen active">
                <h1>Hi Jaan ❤️</h1>
                <p class="typing-text" id="type1">Zoe, aaj aapke liye 50 pages ka sabse bada digital surprise taiyar hai...</p>
                <button class="btn" onclick="startApp()">START JOURNEY ✨</button>
            </div>
            
            <div id="dynamic-content" class="screen">
                <h1 id="dyn-h1"></h1>
                <p class="typing-text" id="dyn-p"></p>
                <button class="btn" id="dyn-btn" onclick="nextStep()">AAGE DEKHO 🌹</button>
            </div>
            
            <div id="final-page" class="screen">
                <h1>Be Mine?</h1>
                <p class="typing-text">Zoe Verma, 50 pages ke safar ke baad bas ek hi sawal... Will you be mine forever? ❤️</p>
                <div style="display:flex; justify-content:center; gap:20px;">
                    <button class="btn" onclick="sayYes()">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#444; color:#fff;" onmouseover="moveNoButton()">NO</button>
                </div>
            </div>
        </div>
    </div>

    <div class="footer-box"><p>💖 I LOVE YOU MERI JAAN ZOE VERMA 💖</p></div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');
        let currentPage = 0;

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
            { h: "Presence", p: "Aapki maujoodgi se hi ghar aur dil dono bhare huye lagte hain." },
            { h: "Connection", p: "Humara rishta sirf baaton ka nahi, dil ka gehra rishta hai." },
            { h: "Support", p: "Aapne mujhe tab samjha jab kisi ne nahi samjha." },
            { h: "Motivation", p: "Aapko dekh kar mujhe life mein behtar karne ki himmat milti hai." },
            { h: "Loyalty", p: "Rehan sirf Zoe ka hai, aur hamesha rahega." },
            { h: "Wada", p: "Main hamesha aapki har baat sununga aur samjhunga." },
            { h: "Bright Side", p: "Andheri raaton mein aap meri roshni ban kar aaye ho." },
            { h: "My World", p: "Maine apni duniya aapke charon taraf basayi hai." },
            { h: "Pure Love", p: "Mera pyar koi dikhava nahi, meri rooh ki sacchai hai." },
            { h: "Admiration", p: "Aapki har ek adaa mere dil ko chu jati hai." },
            { h: "Patience", p: "Aapke intezaar mein bitaya har pal mere liye ibadat hai." },
            { h: "Gentleness", p: "Aapka lehja itna narm hai ki pathar bhi pighal jaye." },
            { h: "Kindness", p: "Duniya ke liye aap ek insaan ho, par mere liye puri duniya." },
            { h: "Protection", p: "Main har dukh se aapko bachane ka wada karta hoon." },
            { h: "Silence", p: "Khamoshi mein bhi hum ek dusre ko samajh lete hain." },
            { h: "Blessing", p: "Upar wale ka sabse bada shukrana ki aap meri ho." },
            { h: "Infinity", p: "Humara safar kabhi khatam nahi hoga, ye anant hai." },
            { h: "Best Friend", p: "Aap meri lover hi nahi, sabse acchi dost bhi ho." },
            { h: "Safe Place", p: "Aapki bahon mein mujhe duniya ka sabse zyada sukoon milta hai." },
            { h: "Healing", p: "Aapke ek 'Hello' se mere saare zakhm bhar jate hain." },
            { h: "Respect", p: "Main sirf aap se pyar nahi karta, aapki bohot izzat bhi karta hoon." },
            { h: "Home", p: "Ghar diwaron se nahi, aapke ehsaas se banta hai." },
            { h: "Sunshine", p: "Aap mere mausam ki pehli dhoop ho." },
            { h: "Priority", p: "Duniya ek taraf, aur mere liye aap hamesha pehle rahoge." },
            { h: "Beauty", p: "Aapki khoobsurti sirat aur surat dono mein hai." },
            { h: "Heartbeat", p: "Meri har dharkan bas aapka hi naam leti hai." },
            { h: "Magic Moments", p: "Humari har choti mulakat mere liye ek tyohar hai." },
            { h: "Stability", p: "Duniya badalti rahe, par Rehan ka Zoe ke liye pyar nahi badlega." },
            { h: "Obsession", p: "Haan, main aapke pyar mein pagal hoon, aur garv hai mujhe." },
            { h: "Future", p: "Main apna har kal sirf aapke saath dekhta hoon." },
            { h: "One & Only", p: "Aap meri pehli aur aakhri pasand ho." },
            { h: "Commitment", p: "Main zindagi bhar aapka sath nibhane ka wada karta hoon." },
            { h: "Soulmate", p: "Hum do jism magar ek jaan hain, Zoe." },
            { h: "Unstoppable", p: "Koi bhi takat humein juda nahi kar sakti." },
            { h: "The Queen", p: "Aap mere dil ke takht ki akeli malkin ho." },
            { h: "Final Thought", p: "Ab 50 pages pure huye, par mera pyar kabhi pura nahi hoga." }
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
            p.style.fontSize = (Math.random() * 20 + 15) + 'px';
            p.style.color = symbol === '❤️' ? '#ff4d6d' : '#fff';
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 6000);
        }

        // Run Hearts and Bubbles continuously
        setInterval(() => {
            createParticle('❤️');
            createParticle('○'); // Bubbles
        }, 400);

        typeEffect(document.getElementById('type1'), "Zoe, aaj aapke liye 50 pages ka sabse bada digital surprise taiyar hai...");
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
