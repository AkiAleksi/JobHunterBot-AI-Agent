# Job Hunt Agent

Tämä projekti sisältää **LangChain-pohjaisen työnhakuagentin**, joka voi:
1. Etsiä työpaikkoja.
2. Analysoida työpaikkailmoituksia.
3. Luoda työhakemuksia (cover letter) käyttäen OpenAI:n LLM:ää.

## Ominaisuudet

- **Job Search**: Simuloi työpaikkojen hakua käyttäjän antaman kyselyn perusteella.
- **Job Analysis**: Analysoi työpaikkailmoituksen ja poimii siitä keskeiset tiedot.
- **Cover Letter Generator**: Luo ammattimaisen työhakemuksen tiettyä työpaikkaa varten.

## Käyttöohjeet

### 1. Asenna riippuvuudet
Varmista, että sinulla on Python 3.10+ asennettuna. Asenna tarvittavat kirjastot:
```bash
pip3 install langchain langchain-community python-dotenv
```
2. Aseta OpenAI API -avain
Luo projektihakemistoon .env-tiedosto ja lisää sinne OpenAI API -avaimesi:

OPEN_API_KEY=your_openai_api_key

3. lataa openAI langchain ja venv

python3 -m venv venv
source venv/bin/activate
pip install openai langchain langchain-community python-dotenv


4. Suorita koodi Suorita koodi seuraavalla komennolla:

python3 JobHUnt.py

5. Hakukirjeen tallennus
Kun koodi suoritetaan, hakukirje tallennetaan tiedostoon cover_letter.txt.

Tiedostot
JobHunt.py: Pääohjelma, joka sisältää työnhakuagentin.
cover_letter.txt: Tiedosto, johon luotu hakukirje tallennetaan.

Huomioita
Työpaikkahaku: Nykyinen koodi simuloi työpaikkahakua. Voit integroida oikean API:n (esim. LinkedIn, Indeed) päivittämällä search_jobs-funktion.
Hakukirjeen luonti: Hakukirjeen sisältö luodaan OpenAI:n LLM:llä.

Huomioita
Työpaikkahaku: Nykyinen koodi simuloi työpaikkahakua. Voit integroida oikean API:n (esim. LinkedIn, Indeed) päivittämällä search_jobs-funktion.
Hakukirjeen luonti: Hakukirjeen sisältö luodaan OpenAI:n LLM:llä.
Lisenssi
