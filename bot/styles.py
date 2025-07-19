def afficher_compteurs(compteurs, style):
    if style == 1:
        return f"❤️ : {compteurs['❤️']}\n♦️ : {compteurs['♦️']}\n♣️ : {compteurs['♣️']}\n♠️ : {compteurs['♠️']}"
    elif style == 2:
        return f"[ ❤️={compteurs['❤️']} | ♦️={compteurs['♦️']} | ♣️={compteurs['♣️']} | ♠️={compteurs['♠️']} ]"
    elif style == 3:
        return f"❤️({compteurs['❤️']}) ♦️({compteurs['♦️']}) ♣️({compteurs['♣️']}) ♠️({compteurs['♠️']})"
    elif style == 4:
        return f"🔢 Compteurs:\n❤️={compteurs['❤️']}\n♦️={compteurs['♦️']}\n♣️={compteurs['♣️']}\n♠️={compteurs['♠️']}"
    elif style == 5:
        return f"🧮❤️:{compteurs['❤️']} ♦️:{compteurs['♦️']} ♣️:{compteurs['♣️']} ♠️:{compteurs['♠️']}"
    else:
        return f"❤️ : {compteurs['❤️']}\n♦️ : {compteurs['♦️']}\n♣️ : {compteurs['♣️']}\n♠️ : {compteurs['♠️']}"

def count_symbols(texte):
    return [s for s in texte if s in '❤️♦️♣️♠️']