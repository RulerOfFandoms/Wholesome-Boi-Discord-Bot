import random

def Affirmation():  #affirmations
    global AffirmationList
    global respond
    AffirmationList = [
'I am exactly where I need to be right now',
'I’m grateful for adversity because it allows me to grow',
'My strength is greater  than my struggles',
'I will let go of the things that I cannot control',
'I am enough',
'I love myself and my body for who I am',
'I am worthy of great things', 'I am strong',
'I am in charge of my own self-worth',
'I am surrounded by love',
'I can create the life I dream of',
'There are endless opportunities around me',
'I am becoming more persistent',
'I am finding myself more fearless of failure',
'I am becoming more focused and driven',
'I will find a way to succeed',
'I can do amazing things',
"I'm allowed to take up space.",
"My past is not a reflection of my future.",
"I am strong enough to make my own decisions.",
"I'm in control of how I react to others.",
"I'm courageous and stand up for myself.",
"Today I choose to create magic, not excuses.",
"I am comfortable asking for what I want because I know I deserve it.",
"Today I choose to focus only on what I can control.",
"I surround myself around love and light.",
"I remove all negativity from my life. I’m making space for success.",
"I embrace my full potential, even when it makes others uncomfortable."
]
    respond = random.choice(AffirmationList)
    return respond


def Quotes():  #wholesome quotes
    global QuotesList
    global respond
    QuotesList = [
"https://i.pinimg.com/236x/83/bc/b2/83bcb2baa3efc8f135ad79bb7e217159.jpg",
'''We cannot solve problems with the kind of thinking we employed when we came up with them.
— Albert Einstein''',
'''Learn as if you will live forever, live like you will die tomorrow. 
— Mahatma Gandhi''',
'''Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.” 
— Mark Twain''',
'''When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.
— Eleanor Roosevelt''',
'''When you change your thoughts, remember to also change your world.
—Norman Vincent Peale''',
"https://i.pinimg.com/236x/18/3f/2d/183f2d017d86d4ec606d6c3601c44483.jpg",
"https://i.pinimg.com/236x/79/1c/9e/791c9e68ef0ef527e9f4d5d490ac222c.jpg",
"https://i.pinimg.com/236x/87/be/c1/87bec1393ce3806cea40c022b612956c.jpg",
"https://i.pinimg.com/236x/99/3f/81/993f81854c6d55455290ed786746c313.jpg",
'''Your life is yours no matter what other's think''',
"https://i.pinimg.com/236x/c3/40/e3/c340e38848d5f44beb91f5d4ae0d0591.jpg",
"https://i.pinimg.com/236x/50/7a/6b/507a6b8da62cd0c46e23c35e3694a6bd.jpg",
"https://i.pinimg.com/236x/e5/d3/d5/e5d3d538542205f47b4efa2584526978.jpg",
"https://i.pinimg.com/236x/b4/d7/04/b4d704b8efdac38a16d7b594d4efd2e3.jpg",
"https://i.pinimg.com/236x/81/36/e2/8136e29ab69e7d21a51c096c49e20a7e.jpg",
"https://i.pinimg.com/236x/74/3e/3e/743e3e622a25e75876bcfb2f46fb18e7.jpg",
"https://i.pinimg.com/236x/c5/b7/a0/c5b7a03fef13f645955ac702eca6092b.jpg",
"https://i.pinimg.com/236x/3e/0f/5d/3e0f5d82a3daf2594e3086750c388a92.jpg",
"https://i.pinimg.com/236x/af/72/49/af7249704f59dfeb747e5150584c97a4.jpg",
"https://i.pinimg.com/236x/23/a4/2b/23a42b032849957c52726e20ffe1546e.jpg",
"https://i.pinimg.com/236x/1e/c2/36/1ec2369ddfdf43dbe1fd73bf2199923d.jpg",
"https://i.pinimg.com/236x/ad/36/fc/ad36fc547f9d3abac9e4ddc92ba95010.jpg",
"https://i.pinimg.com/236x/28/dc/06/28dc06cfe44cd274e97c6423d1586307.jpg",
"https://i.pinimg.com/236x/88/12/6e/88126eee68ee24f6a5b6947923069e98.jpg",
"https://i.pinimg.com/236x/d6/5b/eb/d65bebb54bf3274dbe7fdce919805b1a.jpg",
"https://i.pinimg.com/236x/52/7c/13/527c138c435c8401c8507c4e461e7863.jpg",
        "There is no growth without 'failure'. The only thing where it is truly a failure is when you give up trying."
]
    respond = random.choice(QuotesList)
    return respond


def Gay(): # wholesome gay images
    global Images
    global respond
    Images = [
"https://i.pinimg.com/236x/69/dd/a8/69dda8c7967d042b037015111390916a.jpg",
"https://i.pinimg.com/564x/b1/22/94/b122945c75724f28c42892038fcc5605.jpg",  #https://stackoverflow.com/questions/57451177/python3-create-list-of-image-in-a-folder
"https://i.pinimg.com/236x/a5/eb/3a/a5eb3ae195016fcb5af1ba854439ccdd.jpg",
"https://i.pinimg.com/236x/49/2b/98/492b9829249daaebaaab549c7b48eb44.jpg",
"https://i.pinimg.com/236x/fa/cd/0c/facd0c3d269778cf69f035e87df4ba55.jpg",
"https://i.pinimg.com/236x/7d/51/a3/7d51a38f0525ebcd5a5c5709a77b270d.jpg",
"https://i.pinimg.com/236x/15/b2/35/15b2359bbb2673d617b0ecca22a28d7c.jpg",
"https://i.pinimg.com/236x/8d/0a/83/8d0a839e981c32113f2e60a8ff968ba6.jpg",
"https://i.pinimg.com/236x/e6/89/d0/e689d0c32f21c24f343d44a8b3a9c318.jpg",
"https://i.pinimg.com/236x/5f/b8/54/5fb8542834714d15c9f5f4c13692d001.jpg",
"https://i.pinimg.com/236x/00/56/c2/0056c2ab95a819c52eb926846cfb3ca9.jpg",
"https://i.pinimg.com/236x/60/2d/02/602d02e000dd5cc97fd31b487ff990d3.jpg",
"https://i.pinimg.com/564x/78/e6/68/78e6683b79ddef88971e79e3176e5845.jpg",
"https://i.pinimg.com/236x/a4/2d/ed/a42deddaea8cab938137c9690474aaae.jpg",
"https://i.pinimg.com/236x/15/0f/b6/150fb60c052cfe5cb90449b1240a2819.jpg",
"https://i.pinimg.com/236x/30/33/da/3033da39afe8247f75a187c110512e12.jpg",
"https://i.pinimg.com/236x/ef/ce/bc/efcebc943f46a269839ee4f5c019b317.jpg",
"https://i.pinimg.com/236x/0a/eb/c1/0aebc1853103b062ead3122c835caebf.jpg",
"https://i.pinimg.com/236x/06/67/ef/0667efacaacf846815bfd267e05db841.jpg",
"https://i.pinimg.com/236x/71/70/65/7170657707135dc6cf3b0cd0eba475ed.jpg",
"https://i.pinimg.com/236x/c8/71/0f/c8710f9fddfdc8c6f1a5072027e67275.jpg",
"https://i.pinimg.com/564x/32/f9/a3/32f9a3e12331ab68f8722b51e34afca2.jpg",
"https://i.pinimg.com/564x/69/5a/33/695a33faf1316498169b12c1a532b74b.jpg",
"https://i.pinimg.com/236x/ae/da/01/aeda015481b0de1ce1da4ed629bb9afd.jpg",
"https://i.pinimg.com/236x/1e/2c/26/1e2c26ce18398f4be76b6949c41c2f4e.jpg",
"https://i.pinimg.com/236x/ce/87/c6/ce87c6bfa511e9b63eaf53dc9f7fd2b9.jpg",
"https://i.pinimg.com/236x/f0/36/c3/f036c3e98208e57a137b7804831422ae.jpg"
]
    respond = random.choice(Images)
    return respond

def BuzzBuzz():  #bee images
    global Beez
    global respond
    Beez = [
"https://i.pinimg.com/236x/7c/75/fc/7c75fcc2d9031bb7b139f164655fbd0f.jpg",
"https://i.pinimg.com/236x/ae/9d/18/ae9d1854dc5aae9be30ce81a43349bc1.jpg",
"https://i.pinimg.com/236x/cc/ab/69/ccab6919f88a41d5ef94183d844e7e79.jpg",
"https://i.pinimg.com/236x/67/2d/0c/672d0c0740e039587d9a6114e692d4f1.jpg",
"https://i.pinimg.com/236x/79/87/24/79872482452e4db6344c5e1a8988d42b.jpg",
"https://i.pinimg.com/236x/e3/f8/1c/e3f81c78e632bbd704916e26b49f1fc2.jpg",
"https://i.pinimg.com/236x/bb/77/d7/bb77d70618de613ab86387b146fc513c.jpg",
"https://i.pinimg.com/236x/37/6a/c4/376ac49af3d3da415d8889c5130036c2.jpg",
"https://i.pinimg.com/236x/e9/0a/96/e90a961c4bc0ffd3bb868a6cb80628e7.jpg",
"https://i.pinimg.com/236x/98/a0/f5/98a0f5a09ca6aef845c6ccda8be6e7a9.jpg",
"https://i.pinimg.com/236x/ca/b2/b1/cab2b18c1521e13a1f68dc26211a59de.jpg",
"https://i.pinimg.com/236x/d9/0c/c6/d90cc6e5860b7f0d9172ee2481d20786.jpg",
"https://i.pinimg.com/236x/54/94/ac/5494ac45a4e98fb6c4ee772d3df87c09.jpg",
"https://i.pinimg.com/236x/02/b9/b9/02b9b964ed61ef787f79e44de97af9af.jpg",
"https://i.pinimg.com/236x/75/cd/27/75cd27575a9c74ee13b77bdcbf9e9a17.jpg",
"https://i.pinimg.com/236x/72/38/16/7238165dfc48983a893d15455104702a.jpg",
"https://i.pinimg.com/236x/01/61/00/016100c3366e0c1fe83b390cf5719654.jpg",
"https://i.pinimg.com/236x/33/d8/6f/33d86feeff6d2fb2f0438c97924a085d.jpg",
"https://i.pinimg.com/236x/86/9d/5a/869d5a7668b3080f565e48bea538eee0.jpg",
"https://i.pinimg.com/236x/27/1f/17/271f17020fc3d38aecd9cea74e837c48.jpg",
"https://i.pinimg.com/236x/9d/85/3e/9d853e37fcc9fe7faf81c05fb06b3c4c.jpg",
"https://i.pinimg.com/236x/e3/56/ce/e356ce9b93a0a4b6b9cfd4e5928cc044.jpg",
"https://i.pinimg.com/236x/7d/3f/b9/7d3fb94e9ae69c3238f7ebd93b6e1b4f.jpg",
"https://i.pinimg.com/236x/0f/20/ff/0f20ffb24bea62c724886b2e977e5e4e.jpg",
"https://i.pinimg.com/236x/b8/34/d9/b834d9ab9bb7635a9856581e8cbea621.jpg",
"https://i.pinimg.com/236x/3a/42/de/3a42de3da73a8a038cf34f858975f428.jpg",
"https://i.pinimg.com/236x/25/e5/57/25e5579868a709b35f986a0ea2454221.jpg",
"https://i.pinimg.com/236x/5c/3e/ab/5c3eab718bcdc1456768e6858ea5283b.jpg",
"https://i.pinimg.com/236x/02/23/3a/02233a1a0da3ca6d3da3b8c1c226103c.jpg",
"https://i.pinimg.com/236x/94/ca/b3/94cab35fea96084cdcbecae33c9c4bca.jpg",
"https://i.pinimg.com/236x/12/06/2a/12062a5918dfd8458cf8ca99d40778e6.jpg",
"https://i.pinimg.com/236x/8c/c9/b3/8cc9b312a3acdead6dadbf7241ead365.jpg",
"https://i.pinimg.com/236x/34/2d/e3/342de3f1e58328813ac9277e45eca53b.jpg",
"https://i.pinimg.com/236x/8c/80/90/8c8090aa28c38c3fbcdd2918085d290e.jpg",
"https://i.pinimg.com/236x/86/9d/5a/869d5a7668b3080f565e48bea538eee0.jpg",
"https://i.pinimg.com/236x/68/b5/64/68b5649b36464a7c7d1022dcc9dbae87.jpg",
"https://i.pinimg.com/236x/0f/20/ff/0f20ffb24bea62c724886b2e977e5e4e.jpg",
"https://i.pinimg.com/236x/c6/38/da/c638dab02393703905680b19c22f7138.jpg"

]
    respond = random.choice(Beez)
    return respond