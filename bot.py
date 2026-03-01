async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text.lower() # User ka message lowercase mein
    
    # Check karein ki kya user ne 'dragon ball' likha hai
    if "dragon ball" in user_msg or "goku" in user_msg or "vegeta" in user_msg:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
        
        # Dragon Ball search query
        search_url = f"https://api.jikan.moe/v4/anime?q={user_msg}&limit=1"
        
        try:
            response = requests.get(search_url, timeout=15).json()
            if response.get('data'):
                anime = response['data'][0]
                # ... (baaki details nikalne wala code same rahega)
                title = anime.get('title')
                img_url = anime['images']['jpg']['large_image_url']
                
                caption = f"🐉 *DRAGON BALL SPECIAL*\n\n🎬 *Name:* {title}\n⭐ *Score:* {anime.get('score')}\n🔥 *Status:* {anime.get('status')}"
                await update.message.reply_photo(photo=img_url, caption=caption, parse_mode='Markdown')
            else:
                await update.message.reply_text("Dragon Ball ki ye series nahi mili! 🐉")
        except:
            await update.message.reply_text("Technical issue! Dubara try karein.")
            
    else:
        # Agar user kuch aur likhe toh ye reply dega
        await update.message.reply_text("❌ Main sirf **Dragon Ball** ka expert hoon! Mujhse sirf Goku ya Dragon Ball ke baare mein puchiye. 🐉🔥", parse_mode='Markdown')
      
