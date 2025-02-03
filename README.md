# Fine-tuning Whisper for Polish voice commands

## Results
### Word Error Rate on the test set:

| Base model | Fine-tuned model |
|------------|------------------|
| 0.8435 | 0.3176 |

### Example sentences:

| Reference | Base model | Fine-tuned model |
|-----------|------------|------------------|
| wyślij maila do mojego brata i przypomnij o rocznicy ślubu | wysli myę latą mojego biata i przypamni o nici ślubu | wyślij maila do mojego bryata i przypomnij mi o lepszy ślubu |
| przypomnij mi o jutrzejszym spotkaniu godzinę wcześniej | przypomnij mi o jutrzejszym spotkaniu godzinę wcześniej |  przypomnij mi o jutrzejszym spotkaniu godzina wcześniej |
| graj plejlistę boba dylana | gra i play listę boba dylana | graj playlistę boba delana |
| graj ale jazz autorki sanah | grei, al het rust autoorkisana | graj ale jazz autorki sanah |
| olly posłuchajmy sto jeden i trzy f. m. | oli posłuchajmy sto jeden i trzefam | olly posłuchaj we z to jeden i trzy f. m. |
