import json
import os
from typing import List, Dict

questions = {
    "work": {
        "easy": [
            {"question": "What's your typical work day like?", "tags": ["daily-life", "routine"]},
            {"question": "Do you prefer working from home or in an office?", "tags": ["preferences", "work-environment"]},
            {"question": "What’s your favorite spot to work from (home, cafe, etc.)?", "tags": ["daily-life", "routine"]},
            {"question": "What's your favorite part of your job?", "tags": ["preferences", "job-satisfaction"]},
            {"question": "Do you have a dedicated workspace?", "tags": ["work-environment", "setup"]},
            {"question": "Do you prefer working alone or in a team?", "tags": ["preferences", "collaboration"]},
            {"question": "What tools do you use most at work?", "tags": ["tools", "daily-life"]},
            {"question": "Do you take regular breaks during work?", "tags": ["habits", "routine"]},
            {"question": "What's your favorite time of day to work?", "tags": ["preferences", "productivity"]},
            {"question": "What's your preferred work setup - remote, hybrid, or office?", "tags": ["work-style", "preferences"]},
            {"question": "What productivity apps do you use?", "tags": ["tools", "productivity"]},
            {"question": "How's your home office setup?", "tags": ["workspace", "remote-work"]},
            {"question": "Do you listen to music while working?", "tags": ["habits", "productivity"]},
            {"question": "What's your favorite collaboration tool?", "tags": ["tools", "teamwork"]},
            {"question": "How do you handle work notifications?", "tags": ["communication", "boundaries"]},
            {"question": "Are you interested in startups?", "tags": ["career", "startups"]},
            {"question": "What's your ideal work schedule?", "tags": ["schedule", "preferences"]}
        ],
        "medium": [
            {"question": "How do you handle work-related stress?", "tags": ["stress-management", "wellness"]},
            {"question": "What's the most interesting project you've worked on?", "tags": ["projects", "experiences"]},
            {"question": "How do you maintain work-life balance?", "tags": ["balance", "lifestyle"]},
            {"question": "What skills are most valuable in your field?", "tags": ["skills", "career"]},
            {"question": "Have you noticed any trends in your field or hobby lately?", "tags": ["industry", "changes"]},
            {"question": "What's your approach to time management?", "tags": ["time-management", "productivity"]},
            {"question": "How do you handle difficult colleagues?", "tags": ["interpersonal", "challenges"]},
            {"question": "What's your experience with remote work?", "tags": ["remote-work", "adaptation"]},
            {"question": "How do you stay organized at work?", "tags": ["organization", "productivity"]},
            {"question": "What motivates you in your work?", "tags": ["motivation", "career"]},
            {"question": "How do you feel about the four-day work week?", "tags": ["work-life", "trends"]},
            {"question": "If you could pick any job for a day, what would it be?", "tags": ["freelance", "career"]},
            {"question": "How do you network in the digital age?", "tags": ["networking", "career"]},
            {"question": "What's your take on workplace culture?", "tags": ["culture", "workplace"]},
            {"question": "How do you stay productive while working remotely?", "tags": ["productivity", "remote-work"]},
            {"question": "What's your experience with digital nomad life?", "tags": ["lifestyle", "remote-work"]},
            {"question": "How do you handle zoom fatigue?", "tags": ["remote-work", "wellness"]},
            {"question": "What's your approach to personal branding?", "tags": ["branding", "career"]},
            {"question": "How do you upskill yourself?", "tags": ["learning", "development"]},
            {"question": "What's your view on workplace flexibility?", "tags": ["work-style", "preferences"]}
        ],
        "hard": [
            {"question": "How has your career path evolved over time?", "tags": ["career-path", "growth"]},
            {"question": "If you could start a passion project, what would it be?", "tags": ["leadership", "philosophy"]},
            {"question": "How do you drive innovation in your role?", "tags": ["innovation", "leadership"]},
            {"question": "What's your approach to mentoring others?", "tags": ["mentoring", "leadership"]},
            {"question": "How do you handle ethical dilemmas at work?", "tags": ["ethics", "decision-making"]},
            {"question": "What's your vision for your industry's future?", "tags": ["vision", "future"]},
            {"question": "How do you measure success in your career?", "tags": ["success", "goals"]},
            {"question": "What's your strategy for staying relevant in your field?", "tags": ["strategy", "career"]},
            {"question": "How do you approach organizational change?", "tags": ["change-management", "leadership"]},
            {"question": "What’s the most fun idea you’ve ever had at work?", "tags": ["legacy", "career-goals"]}
        ]
    },
    "hobbies": {
        "easy": [
            {"question": "What do you like to do in your free time?", "tags": ["leisure", "interests"]},
            {"question": "Do you have any regular hobbies?", "tags": ["activities", "routine"]},
            {"question": "Do you prefer indoor or outdoor activities?", "tags": ["preferences", "activities"]},
            {"question": "What’s a hobby you wish you had more time for?", "tags": ["frequency", "routine"]},
            {"question": "Have you ever thought about starting a collection? If so, what would it be?", "tags": ["collecting", "interests"]},
            {"question": "What's your favorite weekend activity?", "tags": ["weekend", "leisure"]},
            {"question": "Do you play any sports?", "tags": ["sports", "activities"]},
            {"question": "Do you have any creative hobbies?", "tags": ["creativity", "interests"]},
            {"question": "What music do you listen to?", "tags": ["music", "entertainment"]},
            {"question": "Do you prefer solo or group activities?", "tags": ["preferences", "social"]},
            {"question": "What’s a fun activity you recently tried for the first time?", "tags": ["interests", "entertainment"]},
            {"question": "Do you have a favorite spot or place for your hobbies (like a park, cafe, or studio)?", "tags": ["preferences", "leisure"]}
        ],
        "medium": [
            {"question": "How did you discover your favorite hobby?", "tags": ["discovery", "interests"]},
            {"question": "What skills have you developed through your hobbies?", "tags": ["skills", "development"]},
            {"question": "How do you make time for your hobbies?", "tags": ["time-management", "balance"]},
            {"question": "What hobby would you like to try next?", "tags": ["aspirations", "interests"]},
            {"question": "Have your hobbies changed over the years?", "tags": ["changes", "growth"]},
            {"question": "Have you ever faced a funny or unexpected challenge while enjoying your hobbies?", "tags": ["challenges", "learning"]},
            {"question": "How do your hobbies help you relax?", "tags": ["relaxation", "wellness"]},
            {"question": "What’s the most unique or unexpected tool you’ve used for a hobby?", "tags": ["equipment", "resources"]},
            {"question": "Have you made friends through your hobbies?", "tags": ["social", "connections"]},
            {"question": "What's your proudest achievement in your hobby?", "tags": ["achievements", "satisfaction"]},
            {"question": "If you could teach your hobby to someone, how would you do it?", "tags": ["social", "connections"]},
            {"question": "What’s the best memory you have related to your hobby?", "tags": ["satisfaction"]}
        ],
        "hard": [
            {"question": "How have your hobbies shaped your personality?", "tags": ["personal-growth", "impact"]},
            {"question": "What life lessons have you learned from your hobbies?", "tags": ["lessons", "wisdom"]},
            {"question": "How do your hobbies reflect your values?", "tags": ["values", "reflection"]},
            {"question": "What role do hobbies play in personal development?", "tags": ["development", "growth"]},
            {"question": "How do you balance multiple interests?", "tags": ["balance", "time-management"]},
            {"question": "What drives your passion for your hobbies?", "tags": ["passion", "motivation"]},
            {"question": "How do your hobbies contribute to your well-being?", "tags": ["well-being", "impact"]},
            {"question": "What’s the most surprising thing your hobby has taught you about yourself?", "tags": ["sacrifices", "commitment"]},
            {"question": "How do you see your hobbies evolving in the future?", "tags": ["future", "growth"]},
            {"question": "If you could create a community or club around your hobby, what would it look like?", "tags": ["legacy", "impact"]},
            {"question": "Have your hobbies ever led you to an unexpected opportunity or experience?", "tags": ["future", "growth"]},
            {"question": "How has your hobby inspired you to try something completely new?", "tags": ["legacy", "impact"]}
        ]
    },
    "travel": {
        "easy": [
            {"question": "Do you enjoy traveling?", "tags": ["preferences", "general"]},
            {"question": "Do you prefer mountains or beaches?", "tags": ["preferences", "destinations"]},
            {"question": "What's your favorite way to travel?", "tags": ["transportation", "preferences"]},
            {"question": "Do you prefer domestic or international travel?", "tags": ["preferences", "destinations"]},
            {"question": "When was the last time you went on a trip, and where did you go?", "tags": ["frequency", "habits"]},
            {"question": "Do you like to take photos while traveling?", "tags": ["activities", "memories"]},
            {"question": "What's your ideal trip length?", "tags": ["preferences", "planning"]},
            {"question": "Do you prefer to travel alone or with others?", "tags": ["preferences", "social"]},
            {"question": "Have you been to many countries?", "tags": ["experience", "international"]},
            {"question": "Do you like trying local food when traveling?", "tags": ["food", "experiences"]},
            {"question": "Have you ever gotten travel inspiration from social media?", "tags": ["social-media", "content"]},
            {"question": "What travel apps do you use?", "tags": ["apps", "planning"]},
            {"question": "Are you into staycations?", "tags": ["local", "trends"]},
            {"question": "Do you prefer solo or group trips?", "tags": ["preferences", "style"]},
            {"question": "What's your favorite booking platform?", "tags": ["planning", "apps"]},
            {"question": "Do you create travel content?", "tags": ["content", "social-media"]},
            {"question": "Are you interested in workations?", "tags": ["remote-work", "trends"]},
            {"question": "How do you document your travels?", "tags": ["memories", "content"]},
            {"question": "What's your ideal weekend getaway?", "tags": ["short-trips", "preferences"]},
            {"question": "Do you use travel reward programs?", "tags": ["rewards", "planning"]},
            {"question": "What’s a destination that’s on your bucket list?", "tags": ["short-trips", "preferences"]},
            {"question": "Do you prefer planning every detail or going with the flow on trips?", "tags": ["rewards", "planning"]}
        ],
        "medium": [
            {"question": "What's the most interesting place you've visited?", "tags": ["experiences", "memories"]},
            {"question": "How do you plan your trips?", "tags": ["planning", "organization"]},
            {"question": "What's your most memorable travel experience?", "tags": ["memories", "experiences"]},
            {"question": "How do you handle language barriers while traveling?", "tags": ["challenges", "communication"]},
            {"question": "What's your approach to travel budgeting?", "tags": ["planning", "finance"]},
            {"question": "What do you look for in a travel destination?", "tags": ["preferences", "decision-making"]},
            {"question": "How do you deal with travel stress?", "tags": ["stress-management", "challenges"]},
            {"question": "What’s the funniest or most unexpected thing that happened during your travels?", "tags": ["stories", "experiences"]},
            {"question": "How do you maintain comfort while traveling?", "tags": ["comfort", "preferences"]},
            {"question": "What's your favorite travel memory?", "tags": ["memories", "experiences"]},
            {"question": "How do you feel about sustainable tourism?", "tags": ["sustainability", "responsibility"]},
            {"question": "What's your experience with travel hacks?", "tags": ["tips", "planning"]},
            {"question": "How do you balance travel and work?", "tags": ["work-life", "balance"]},
            {"question": "What's your approach to travel budgeting?", "tags": ["finance", "planning"]},
            {"question": "Do you like sharing your travel experiences online or keeping them private?", "tags": ["social-media", "habits"]},
            {"question": "What's your take on influencer tourism?", "tags": ["social-media", "trends"]},
            {"question": "How do you research destinations?", "tags": ["planning", "research"]},
            {"question": "What's your experience with last-minute trips?", "tags": ["spontaneity", "planning"]},
            {"question": "How do you pack for trips?", "tags": ["preparation", "tips"]},
            {"question": "What's your view on slow travel?", "tags": ["style", "trends"]},
            {"question": "What’s the best meal you’ve ever had while traveling?", "tags": ["preparation", "tips"]},
            {"question": "What’s your go-to method for finding hidden gems at a destination?", "tags": ["style", "trends"]}
        ],
        "hard": [
            {"question": "How has traveling changed your worldview?", "tags": ["perspective", "impact"]},
            {"question": "What cultural differences have impacted you most?", "tags": ["culture", "impact"]},
            {"question": "How do you connect with different cultures?", "tags": ["culture", "connection"]},
            {"question": "What have you learned about yourself through travel?", "tags": ["self-discovery", "growth"]},
            {"question": "How has travel influenced your life choices?", "tags": ["influence", "decisions"]},
            {"question": "What role does travel play in personal growth?", "tags": ["growth", "development"]},
            {"question": "How do you balance travel with other life commitments?", "tags": ["balance", "priorities"]},
            {"question": "What’s a meaningful lesson you’ve learned from your travel experiences?", "tags": ["philosophy", "insights"]},
            {"question": "How do you think your travel style has changed over the years?", "tags": ["future", "change"]},
            {"question": "What impact does tourism have on local cultures?", "tags": ["impact", "culture"]}
        ]
    },
    "food": {
        "easy": [
            {"question": "What's your favorite type of food?", "tags": ["preferences", "cuisine"]},
            {"question": "Do you enjoy cooking?", "tags": ["cooking", "hobbies"]},
            {"question": "What's your favorite meal of the day?", "tags": ["preferences", "meals"]},
            {"question": "Do you prefer eating out or at home?", "tags": ["preferences", "habits"]},
            {"question": "What's your go-to snack?", "tags": ["preferences", "snacks"]},
            {"question": "Do you have any dietary restrictions?", "tags": ["diet", "health"]},
            {"question": "What's your favorite restaurant?", "tags": ["preferences", "dining"]},
            {"question": "Do you like trying new foods?", "tags": ["adventure", "preferences"]},
            {"question": "What's your favorite dessert?", "tags": ["preferences", "desserts"]},
            {"question": "Do you drink coffee or tea?", "tags": ["preferences", "beverages"]},
            {"question": "What's your favorite food delivery app?", "tags": ["delivery", "apps"]},
            {"question": "Do you ever get recipe ideas from social media?", "tags": ["social-media", "content"]},
            {"question": "Are you into meal kit services?", "tags": ["services", "cooking"]},
            {"question": "What's your go-to café?", "tags": ["cafes", "social"]},
            {"question": "Do you take food photos for social media?", "tags": ["social-media", "habits"]},
            {"question": "What's your favorite brunch spot?", "tags": ["dining", "social"]},
            {"question": "Have you ever tried making a viral recipe?", "tags": ["trends", "social-media"]},
            {"question": "Do you watch mukbang videos?", "tags": ["content", "trends"]},
            {"question": "What's your favorite fusion food?", "tags": ["cuisine", "trends"]},
            {"question": "Are you into craft beverages?", "tags": ["drinks", "trends"]},
            {"question": "What’s a dish you could eat every day and never get tired of?", "tags": ["diet", "social"]},
            {"question": "What’s the first dish you ever learned to cook?", "tags": ["trends", "interests"]}
        ],
        "medium": [
            {"question": "What's the most interesting dish you've tried?", "tags": ["experiences", "adventure"]},
            {"question": "How has your taste in food evolved?", "tags": ["changes", "preferences"]},
            {"question": "What's your approach to healthy eating?", "tags": ["health", "nutrition"]},
            {"question": "What's your favorite cuisine to cook?", "tags": ["cooking", "cuisine"]},
            {"question": "How did you learn to cook?", "tags": ["learning", "skills"]},
            {"question": "What's your favorite food memory?", "tags": ["memories", "experiences"]},
            {"question": "How do you discover new recipes?", "tags": ["discovery", "cooking"]},
            {"question": "What's your favorite cooking technique?", "tags": ["cooking", "skills"]},
            {"question": "Do you enjoy meal prepping or cooking spontaneously?", "tags": ["planning", "organization"]},
            {"question": "What's your favorite food tradition?", "tags": ["tradition", "culture"]},
            {"question": "How do you discover new restaurants?", "tags": ["discovery", "dining"]},
            {"question": "What’s your experience with food delivery services?", "tags": ["trends", "delivery"]},
            {"question": "How do you feel about viral food trends?", "tags": ["trends", "social-media"]},
            {"question": "What's your experience with food subscription boxes?", "tags": ["subscription", "services"]},
            {"question": "How do you balance eating out and cooking?", "tags": ["lifestyle", "habits"]},
            {"question": "What's your favorite food content format?", "tags": ["content", "media"]},
            {"question": "How do you feel about plant-based alternatives?", "tags": ["diet", "trends"]},
            {"question": "What's your approach to sustainable eating?", "tags": ["sustainability", "diet"]},
            {"question": "How do you handle dietary preferences when dining out?", "tags": ["diet", "social"]},
            {"question": "What food trends do you want to try?", "tags": ["trends", "interests"]},
            {"question": "What’s the best street food you’ve ever tried?", "tags": ["diet", "social"]},
            {"question": "Is there a restaurant you’ve been wanting to visit for ages?", "tags": ["trends", "interests"]}
        ],
        "hard": [
            {"question": "How does food connect to your cultural identity?", "tags": ["culture", "identity"]},
            {"question": "How can food be used to teach about culture?", "tags": ["relationships", "social"]},
            {"question": "How do you think food habits will change in the future?", "tags": ["future", "society"]},
            {"question": "What's your food philosophy?", "tags": ["philosophy", "beliefs"]},
            {"question": "What’s a food-related tradition that’s meaningful to you?", "tags": ["society", "impact"]},
            {"question": "What ethical considerations guide your food choices?", "tags": ["ethics", "choices"]},
            {"question": "How does food connect different cultures?", "tags": ["culture", "connection"]},
            {"question": "What impact does food have on community?", "tags": ["community", "impact"]},
            {"question": "How do you balance tradition and innovation in food?", "tags": ["tradition", "innovation"]},
            {"question": "What role should food play in education?", "tags": ["education", "society"]},
            {"question": "What’s a food experience that changed the way you think about cooking or eating?", "tags": ["tradition", "innovation"]},
            {"question": "How do you think globalization has impacted local cuisines?", "tags": ["education", "society"]}
        ]
    },
    "tech": {
        "easy": [
            {"question": "What gadgets do you use daily?", "tags": ["devices", "habits"]},
            {"question": "Do you prefer Android or iOS?", "tags": ["preferences", "mobile"]},
            {"question": "How often do you upgrade your phone?", "tags": ["habits", "devices"]},
            {"question": "What apps do you use most?", "tags": ["apps", "usage"]},
            {"question": "Do you enjoy video games?", "tags": ["games", "entertainment"]},
            {"question": "What's your favorite tech device?", "tags": ["preferences", "devices"]},
            {"question": "Do you use social media?", "tags": ["social-media", "communication"]},
            {"question": "What streaming services do you use?", "tags": ["entertainment", "services"]},
            {"question": "Do you have smart home devices?", "tags": ["smart-home", "devices"]},
            {"question": "Do you use cloud storage for your files?", "tags": ["data", "security"]},
            {"question": "What's your take on ChatGPT?", "tags": ["ai", "tools"]},
            {"question": "Have you tried any VR headsets?", "tags": ["vr", "gadgets"]},
            {"question": "What smart home devices do you use?", "tags": ["smart-home", "automation"]},
            {"question": "What's your favorite tech gadget?", "tags": ["gadgets", "preferences"]},
            {"question": "Do you use any AI tools?", "tags": ["ai", "tools"]},
            {"question": "What do you think about foldable phones?", "tags": ["mobile", "trends"]},
            {"question": "Do you use any health tech devices?", "tags": ["health-tech", "gadgets"]}
        ],
        "medium": [
            {"question": "How has technology changed your work life?", "tags": ["work", "impact"]},
            {"question": "What's your approach to digital privacy?", "tags": ["privacy", "security"]},
            {"question": "How do you learn about new technology?", "tags": ["learning", "education"]},
            {"question": "What's your view on social media's impact?", "tags": ["social-media", "society"]},
            {"question": "How do you manage screen time?", "tags": ["health", "habits"]},
            {"question": "What tech skills are you developing?", "tags": ["skills", "learning"]},
            {"question": "How do you stay current with tech trends?", "tags": ["trends", "learning"]},
            {"question": "What's your experience with remote work tools?", "tags": ["work", "tools"]},
            {"question": "How do you evaluate new technology?", "tags": ["evaluation", "decision-making"]},
            {"question": "What's your favorite tech innovation?", "tags": ["innovation", "preferences"]},
            {"question": "How do you feel about the metaverse?", "tags": ["metaverse", "virtual"]},
            {"question": "Have you seen AI-generated content? What do you think about it?", "tags": ["ai", "creativity"]},
            {"question": "How do you protect your digital privacy?", "tags": ["privacy", "security"]},
            {"question": "Have you tried any tools that make tech easier to use, like drag-and-drop platforms?", "tags": ["no-code", "development"]},
            {"question": "How do you feel about social media algorithms?", "tags": ["social-media", "algorithms"]},
            {"question": "What's your view on digital wallets?", "tags": ["fintech", "mobile"]},
            {"question": "How do you feel about subscription-based apps?", "tags": ["apps", "business-model"]},
            {"question": "What tech trends excite you most?", "tags": ["trends", "future"]},
            {"question": "Do you think remote work has made technology more essential?", "tags": ["organization", "digital"]}
        ],
        "hard": [
            {"question": "How will AI impact society?", "tags": ["ai", "future"]},
            {"question": "What ethical concerns do you have about technology?", "tags": ["ethics", "concerns"]},
            {"question": "How do you balance digital and real-world life?", "tags": ["balance", "lifestyle"]},
            {"question": "What role should technology play in education?", "tags": ["education", "society"]},
            {"question": "How might technology change human relationships?", "tags": ["relationships", "impact"]},
            {"question": "Do you think AI will ever surpass human intelligence completely?", "tags": ["future", "philosophy"]},
            {"question": "How should we govern artificial intelligence?", "tags": ["ai", "governance"]},
            {"question": "What's technology's role in solving global challenges?", "tags": ["global", "solutions"]},
            {"question": "How do you see technology evolving in the next decade?", "tags": ["future", "evolution"]},
            {"question": "How has technology influenced the way we share and preserve culture?", "tags": ["culture", "impact"]},
            {"question": "What ethical dilemmas do you think we’ll face with AI in the future?", "tags": ["future", "evolution"]},
            {"question": "How can technology be used to bridge social or economic gaps?", "tags": ["culture", "impact"]}
        ]
    },
    "entertainment": {
        "easy": [
            {"question": "What's your favorite Netflix series?", "tags": ["streaming", "tv-shows"]},
            {"question": "Who’s your favorite YouTuber, and why?", "tags": ["social-media", "content"]},
            {"question": "What's your go-to music streaming platform?", "tags": ["music", "streaming"]},
            {"question": "Are you into any Korean dramas?", "tags": ["k-drama", "tv-shows"]},
            {"question": "Do you follow any content creators?", "tags": ["social-media", "influencers"]},
            {"question": "What's the last show you binged?", "tags": ["tv-shows", "habits"]},
            {"question": "What’s your favorite short-form video platform?", "tags": ["social-media", "short-form"]},
            {"question": "What podcasts do you listen to?", "tags": ["podcasts", "audio"]},
            {"question": "Are you into any anime?", "tags": ["anime", "animation"]},
            {"question": "What's your favorite movie genre?", "tags": ["movies", "preferences"]},
            {"question": "What’s the most rewatchable movie or series for you?", "tags": ["podcasts", "audio"]},
            {"question": "Are you more into live performances or recorded content?", "tags": ["anime", "animation"]},
            {"question": "What’s your favorite movie snack?", "tags": ["movies", "preferences"]}
        ],
        "medium": [
            {"question": "What’s your opinion on user-generated content like reviews or reaction videos?", "tags": ["content", "trends"]},
            {"question": "What do you think about streaming platforms vs traditional TV?", "tags": ["streaming", "media"]},
            {"question": "How has TikTok changed entertainment?", "tags": ["social-media", "impact"]},
            {"question": "What do you think about YouTube shorts and reels?", "tags": ["short-form", "content"]},
            {"question": "How do you discover new music these days?", "tags": ["music", "discovery"]},
            {"question": "What's your take on subscription services?", "tags": ["services", "costs"]},
            {"question": "Do you think binge-watching changes how we experience stories?", "tags": ["habits", "viewing"]},
            {"question": "What makes you subscribe to a content creator?", "tags": ["content", "engagement"]},
            {"question": "How important are reviews in choosing what to watch?", "tags": ["decision-making", "reviews"]},
            {"question": "What's your favorite way to share recommendations?", "tags": ["sharing", "social"]},
            {"question": "How do you balance between watching new content and rewatching old favorites?", "tags": ["content", "engagement"]},
            {"question": "Do you think streaming services are overwhelming with too many options?", "tags": ["decision-making", "reviews"]},
            {"question": "What role does nostalgia play in your entertainment choices?", "tags": ["sharing", "social"]}
        ],
        "hard": [
            {"question": "How does entertainment shape society?", "tags": ["society", "impact"]},
            {"question": "What role should entertainment play in education?", "tags": ["education", "purpose"]},
            {"question": "How has entertainment evolved with technology?", "tags": ["technology", "evolution"]},
            {"question": "What's the future of entertainment?", "tags": ["future", "trends"]},
            {"question": "How does entertainment influence culture?", "tags": ["culture", "influence"]},
            {"question": "What ethical considerations exist in entertainment?", "tags": ["ethics", "considerations"]},
            {"question": "Do you think entertainment is more of a mirror or a shaper of society?", "tags": ["society", "reflection"]},
            {"question": "What impact does entertainment have on youth?", "tags": ["youth", "impact"]},
            {"question": "How do different cultures approach entertainment?", "tags": ["culture", "comparison"]},
            {"question": "How does entertainment contribute to mental well-being or stress relief?", "tags": ["value", "society"]},
            {"question": "What responsibilities do creators have when making impactful content?", "tags": ["youth", "impact"]},
            {"question": "How do global entertainment trends influence local cultures?", "tags": ["culture", "comparison"]},
            {"question": "What’s your take on the line between entertainment and propaganda?", "tags": ["value", "society"]},
        ]
    },
    "lifestyle": {
        "easy": [
            {"question": "What's your typical daily routine?", "tags": ["routine", "daily-life"]},
            {"question": "How do you start your day?", "tags": ["morning", "habits"]},
            {"question": "Do you exercise regularly?", "tags": ["exercise", "health"]},
            {"question": "What's your favorite time of day?", "tags": ["preferences", "daily-life"]},
            {"question": "How do you spend your weekends?", "tags": ["weekend", "leisure"]},
            {"question": "Do you have any daily habits?", "tags": ["habits", "routine"]},
            {"question": "Are you a morning person or a night owl?", "tags": ["sleep", "routine"]},
            {"question": "Do you meal plan?", "tags": ["food", "planning"]},
            {"question": "How do you commute?", "tags": ["transportation", "daily-life"]},
            {"question": "What's your favorite way to relax?", "tags": ["relaxation", "preferences"]},
            {"question": "Do you meal prep?", "tags": ["food", "organization"]},
            {"question": "Are you into fitness challenges?", "tags": ["fitness", "trends"]},
            {"question": "Do you use any wellness apps?", "tags": ["apps", "wellness"]},
            {"question": "What's your favorite workout playlist?", "tags": ["music", "fitness"]},
            {"question": "Do you use any gadgets to track your health?", "tags": ["fitness", "tracking"]},
            {"question": "Are you into mindfulness apps?", "tags": ["wellness", "mental-health"]},
            {"question": "What's your skincare routine like?", "tags": ["self-care", "beauty"]},
            {"question": "Do you follow any wellness influencers?", "tags": ["social-media", "wellness"]},
            {"question": "What's your favorite healthy snack?", "tags": ["food", "health"]},
            {"question": "How do you practice self-care?", "tags": ["wellness", "self-care"]},
            {"question": "Do you have a favorite way to spend your evenings?", "tags": ["social-media", "wellness"]},
            {"question": "What’s your favorite way to unwind after a busy day?", "tags": ["food", "health"]},
            {"question": "Are you more into working out at home or at the gym?", "tags": ["wellness", "self-care"]}
        ],
        "medium": [
            {"question": "How do you maintain work-life balance?", "tags": ["balance", "work-life"]},
            {"question": "What healthy habits have you developed?", "tags": ["health", "habits"]},
            {"question": "How do you manage stress?", "tags": ["stress", "management"]},
            {"question": "Do you follow a budget or have any saving tips?", "tags": ["finance", "planning"]},
            {"question": "How do you stay organized?", "tags": ["organization", "habits"]},
            {"question": "How has your fitness routine changed over time?", "tags": ["fitness", "health"]},
            {"question": "How do you practice self-care?", "tags": ["self-care", "wellness"]},
            {"question": "What's your approach to personal development?", "tags": ["development", "growth"]},
            {"question": "How do you maintain relationships?", "tags": ["relationships", "social"]},
            {"question": "What role does nature play in your lifestyle?", "tags": ["nature", "wellness"]},
            {"question": "How do you manage dating and career?", "tags": ["relationships", "work-life"]},
            {"question": "What's your approach to sustainable living?", "tags": ["sustainability", "lifestyle"]},
            {"question": "How do you deal with burnout?", "tags": ["mental-health", "work-life"]},
            {"question": "What's your take on minimalism?", "tags": ["lifestyle", "trends"]},
            {"question": "How do you maintain friendships as an adult?", "tags": ["relationships", "social"]},
            {"question": "What's your approach to financial wellness?", "tags": ["finance", "planning"]},
            {"question": "How do you handle social media pressure?", "tags": ["social-media", "mental-health"]},
            {"question": "What's your view on work-life integration?", "tags": ["work-life", "balance"]},
            {"question": "How do you stay motivated to exercise?", "tags": ["fitness", "motivation"]},
            {"question": "What's your experience with therapy or counseling?", "tags": ["mental-health", "wellness"]},
            {"question": "How do you manage your downtime effectively?", "tags": ["work-life", "balance"]},
            {"question": "What’s the most rewarding healthy habit you’ve developed?", "tags": ["fitness", "motivation"]},
            {"question": "How do you stay focused on your goals during busy periods?", "tags": ["mental-health", "wellness"]}
        ],
        "hard": [
            {"question": "How has your lifestyle evolved with age?", "tags": ["evolution", "growth"]},
            {"question": "What’s a personal value that shapes how you spend your time?", "tags": ["values", "choices"]},
            {"question": "How does environment influence lifestyle?", "tags": ["environment", "influence"]},
            {"question": "What role does mindfulness play in your life?", "tags": ["mindfulness", "wellness"]},
            {"question": "How do you balance tradition and modernity?", "tags": ["balance", "values"]},
            {"question": "What impact does society have on lifestyle?", "tags": ["society", "impact"]},
            {"question": "How do you maintain authenticity in your lifestyle?", "tags": ["authenticity", "values"]},
            {"question": "What's your philosophy on sustainable living?", "tags": ["sustainability", "philosophy"]},
            {"question": "How do you adapt to life changes?", "tags": ["adaptation", "change"]},
            {"question": "What lifestyle changes have had the biggest impact on your happiness?", "tags": ["legacy", "purpose"]},
            {"question": "How do you think your lifestyle will evolve in the next decade?", "tags": ["sustainability", "philosophy"]},
            {"question": "What’s your perspective on balancing ambition with contentment?", "tags": ["adaptation", "change"]},
            {"question": "Do you believe modern conveniences make life better or more complicated?", "tags": ["legacy", "purpose"]}
        ]
    }
}

def generate_id(category: str, difficulty: str, index: int) -> str:
    """Generate a unique ID for each question"""
    prefix = category[0] if category != "tech" else "te"  # tech는 't'대신 'te' 사용
    return f"{prefix}{difficulty[0]}{index + 1}"

def create_json_files(questions: Dict) -> None:
    """Create JSON files for each category and difficulty level"""
    # 출력 디렉토리 생성
    base_dir = "src/data/topics"
    for difficulty in ["easy", "medium", "hard"]:
        dir_path = os.path.join(base_dir, difficulty)
        os.makedirs(dir_path, exist_ok=True)
        
        # 각 카테고리별 파일 생성
        for category, data in questions.items():
            output_data = {
                "category": category,
                "topics": []
            }
            
            # 해당 난이도의 질문들 처리
            for i, q in enumerate(data[difficulty]):
                question_data = {
                    "id": generate_id(category, difficulty, i),
                    "question": q["question"],
                    "tags": q["tags"]
                }
                output_data["topics"].append(question_data)
            
            # JSON 파일 생성
            filename = os.path.join(dir_path, f"{category}.json")
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2)

if __name__ == "__main__":
    create_json_files(questions)