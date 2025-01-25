# Fine-tuning Whisper for Polish voice commands

## Results
Before tine-tuning:

WER on the test set: 0.8435

|     Ground Truth     |     Transcription     |
|----------------------|-----------------------|
| jaki film jest teraz najwyżej oceniany | Jak i film jest teraz najwyżlioteniony |
| czy są jakieś informacje o prezydenturze | Czy są jakieś informacje o prezetyntu, że |
| usuń następne wydarzenie dzisiaj | Musun na stampę wydarzenie dzisiaj. |
| nowe aktualności | Nowe aktualności. |
| czy mogę zamówić dostawę z tej restauracji | Czy mogę zamówić dostawę ustaj restauracji? |

After fine-tuning:

Word Error Rate (WER) on the test set: 0.3216

|     Ground Truth     |     Transcription     |
|----------------------|-----------------------|
|wyślij maila do mojego brata i przypomnij o rocznicy ślubu | wyślij maila do mojego bryata i przypomnij o leucnicy ślubu |
| przypomnij mi o jutrzejszym spotkaniu godzinę wcześniej | przypomnij mi o jutrzejszym spotkaniu godziny wcześniej |
| graj plejlistę boba dylana | graj playlistę boba delana |
| graj ale jazz autorki sanah | graj ale jazz autorki sanah |
| olly posłuchajmy sto jeden i trzy f. m. | olly posłuchajmy z to jeden i trzy f. m. |
