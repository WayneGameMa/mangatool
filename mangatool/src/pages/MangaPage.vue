<template>
  <q-page class="flex flex-center">
      <div class="menu">
      <!-- Menü zur Einstellung des Titels und der Anzahl der Karten -->
      <q-input
        v-model="pageTitle"
        label="Seitentitel"
        filled
        class="menu__item"
      />
      <q-input
        v-model="numberOfCards"
        label="Anzahl der Seite"
        type="number"
        filled
        class="menu__item"
      />
      <q-input
        v-model="minute_sketch"
        label="Minuten for Skizze"
        type="number"
        filled
        class="menu__item"
      />
      <q-input
        v-model="minute_inking"
        label="Minuten for Inking"
        type="number"
        filled
        class="menu__item"
      />
      <q-input
        v-model="minute_raster"
        label="Minuten for Raster"
        type="number"
        filled
        class="menu__item"
      />
      </div>
      <div class="menu">
        <q-select
        filled
        v-model="week_days"
        multiple
        :values="week_day_options"
        :options="week_day_values"
        label="Wochentage"
        style="width: 250px"
        class="menu__item"
      ></q-select>

      <q-input class="menu__item" filled v-model="start_time" mask="time" :rules="['time']">
        <template v-slot:append>
          <q-icon name="access_time" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-time
                v-model="start_time"
                with-seconds
                format24h
              >
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat></q-btn>
                </div>
              </q-time>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>

      <q-input class="menu__item" filled v-model="end_time" mask="time" :rules="['time']">
        <template v-slot:append>
          <q-icon name="access_time" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-time
                v-model="end_time"
                with-seconds
                format24h
              >
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat></q-btn>
                </div>
              </q-time>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>

      <q-btn @click="updateTitleAndCards(); save()" class="menu__item">Einstellungen speichern</q-btn>
    </div>
    <div>
    <p>Skizze: {{cards_sketch}} Ink: {{cards_ink}} Fertig: {{cards_fertig}}
      <br>Fertigstellung: {{date}}</p>
    </div>

    <!-- Seite-Titel -->
    <h1 class="page-title">{{ pageTitle }}</h1>

    <div class="card-container card--fixedWidth">
      <div v-for="(card, index) in cards"
        :key="index"
        :id = index
        :class="`card ${card}`"
        ref="clickableElement"
      @click="toggleClass(index)">
        
        <div class="card__image" id="card-1">
          <div class="image-overlay">
          </div>
        </div>
        
      </div>
      <q-btn @click="addCard" class="add-card-btn">Neue Karte hinzufügen</q-btn>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import $ from 'jquery';
import { ref } from 'vue';

export default defineComponent({
  name: 'MangaPage',
  data() {
    return {
      date: ref(""),
      pageTitle: ref('Title'), // Default-Titelseite
      numberOfCards: ref(0), // Standardanzahl von Karten
      minute_sketch: ref(30),
      minute_inking: ref(30),
      minute_raster: ref(30),
      cards: ref([]),
      cards_sketch: ref(0),
      cards_ink: ref(0),
      cards_fertig: ref(0),
      week_days: ref([0, 1, 2, 3, 4]),
      week_day_options: [
        'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'
      ],
      week_day_values: [
        0, 1, 2, 3, 4, 5, 6
      ],
      start_time: ref('08:00'),
      end_time: ref('10:00'),
    };
  },
  methods: {
    isActive(className) {
      return this.activeClass === className;
    },
    toggleClass(index) {
      const element = $('#' + index);
      // Ändere den Zustand der ausgewählten Karte
      switch (element.attr('class')) {
        case 'card fertig':
          element.removeClass('fertig');
          element.toggleClass('nothing');
          this.cards_fertig -= 1;
          break;
        case 'card ink':
          element.removeClass('ink');
          element.toggleClass('fertig');
          this.cards_ink -= 1;
          this.cards_fertig += 1;
          break;
        case 'card sketch':
          element.removeClass('sketch');
          element.toggleClass('ink');
          this.cards_sketch -= 1;
          this.cards_ink += 1;
          break;
        case 'card nothing':
          element.removeClass('nothing');
          element.toggleClass('sketch');
          this.cards_sketch += 1;
          break;
        default:
          element.toggleClass('nothing');
          break;
      }
      this.cards[index] = element.attr('class').split(/\s+/)[1]
      localStorage.setItem('cards', JSON.stringify(this.cards)); // Speichere das cards-Array als JSON-String
      console.log(`Klassenname nachher: ${element.attr('class').split(/\s+/)[1]}`);
      this.updateTitleAndCards();
    },
    addCard() {
      this.cards.push('nothing'); // Füge eine neue Karte zum Array hinzu
      this.numberOfCards = this.cards.length;
    },
    updateTitleAndCards() {
      // Setze den Titel der Seite und die Anzahl der Karten basierend auf den Eingabefeldern
      document.title = this.pageTitle;
      if (this.numberOfCards < this.cards.length){
        this.cards = this.cards.slice(0, this.numberOfCards);
      }

      if (this.numberOfCards > this.cards.length){
        const card_len = this.cards.length
        for (let i = 0; i < this.numberOfCards - card_len; i++) {
          this.cards.push('nothing')
        }
      }
      this.save()
    },
    async save(){

      document.title = this.pageTitle;
      if (this.numberOfCards < this.cards.length){
        this.cards = this.cards.slice(0, this.numberOfCards);
      }

      if (this.numberOfCards > this.cards.length){
        const card_len = this.cards.length
        for (let i = 0; i < this.numberOfCards - card_len; i++) {
          this.cards.push('nothing')
        }
      }
   
      let bodyString =`
                {
                "Title": "${this.pageTitle}",
                "NumberPages": ${this.numberOfCards},
                "MinutesSketch": ${this.minute_sketch},
                "MinutesInk": ${this.minute_inking},
                "MinutesRaster": ${this.minute_raster},
                "CardsSketch": ${this.cards_sketch},
                "CardsInk": ${this.cards_ink},
                "CardsRaster": ${this.cards_fertig},
                "Cards": ${JSON.stringify(this.cards)},
                "WeekDays": [${this.week_days}],
                "StartTime": "${this.start_time}",
                "EndTime": "${this.end_time}"
              }
              `;
      console.log(bodyString)
      let requestString =`http://${location.host}:8000/save`;
        
      // 👇️ const response: Response
        
      const response = await fetch(requestString,
                  {
                    method: "POST",
                    headers: {
                              mode: "cors",
                              Accept: "application/json",
                              "Content-Type": "application/json",
                            },
                    body: bodyString,
                  });
      if (!response.ok){
        	consol.log("Fehler Network");
        }

      const feedback = (await response.json());
   
      this.update_date();

    },
    async loadVariablesFromStorage() {
      let requestString =`http://${location.host}:8000/load`;
        
      // 👇️ const response: Response
        
      const response = await fetch(requestString,
                  {
                    method: "POST",
                    headers: {
                              mode: "cors",
                              Accept: "application/json",
                              "Content-Type": "application/json",
                            },
                  });
      if (!response.ok){
        	consol.log("Fehler Network");
        }

      const feedback = (await response.json());
      // Lade die Variablen vom LocalStorage, wenn sie vorhanden sind
      const storedPageTitle = feedback.manga.Title;
      const storedNumberOfCards = feedback.manga.NumberPages;
      const storedCards = feedback.manga.Cards;
      const minute_sketch = feedback.manga.MinutesSketch;
      const minute_ink = feedback.manga.MinutesInk;
      const minute_raster = feedback.manga.MinutesRaster;
      const cards_sketch = feedback.manga.CardsSketch;
      const cards_ink = feedback.manga.CardsInk;
      const cards_fertig = feedback.manga.CardsRaster;
      const week_days = feedback.manga.WeekDays; 
      this.start_time = feedback.manga.StartTime;
      this.end_time = feedback.manga.EndTime;

      if (storedPageTitle) {
        this.pageTitle = storedPageTitle;
      }
      if (minute_sketch) {
        this.minute_sketch = parseInt(minute_sketch, 10);
      }
      if (minute_ink) {
        this.minute_inking = parseInt(minute_ink, 10);
      }
      if (minute_raster) {
        this.minute_raster = parseInt(minute_raster, 10);
      }
      if (cards_sketch) {
        this.cards_sketch = parseInt(cards_sketch, 10);
      }
      if (cards_ink) {
        this.cards_ink = parseInt(cards_ink, 10);
      }
      if (cards_fertig) {
        this.cards_fertig = parseInt(cards_fertig, 10);
      }

      if (storedNumberOfCards) {
        this.numberOfCards = parseInt(storedNumberOfCards, 10);
        this.cards = new Array(Number(storedNumberOfCards)).fill('nothing');
      }

      if (storedCards) {
        this.cards = storedCards; // Wiederherstellen des cards-Arrays aus dem JSON-String
      }
      if (week_days) {
        this.week_days = week_days; // Wiederherstellen des cards-Arrays aus dem JSON-String
      }
      this.update_date();
    },
    update_date () {
      const startTimeArr = this.start_time.split(':').map(x => parseInt(x));
      const endTimeArr = this.end_time.split(':').map(x => parseInt(x));
      const startTimeDate = new Date();
      startTimeDate.setHours(startTimeArr[0], startTimeArr[1], 0, 0);
      const endTimeDate = new Date();
      endTimeDate.setHours(endTimeArr[0], endTimeArr[1], 0, 0);
      const currentDate = new Date();
      const number = this.numberOfCards - this.cards_fertig  - this.cards_sketch - this.cards_ink;
     
      let totalTimeMinutes = (this.minute_sketch + this.minute_inking + this.minute_raster) * number;
      totalTimeMinutes += (this.minute_inking + this.minute_raster) * this.cards_sketch;
      totalTimeMinutes += (this.minute_raster) * this.cards_ink;
      console.log(totalTimeMinutes);

      const workDurationMinutes = (endTimeDate.getHours() - startTimeDate.getHours()) * 60 + (endTimeDate.getMinutes() - startTimeDate.getMinutes());

      const work_percent = (workDurationMinutes / (24 * 60)) * (this.week_days.length / 7);
      console.log(work_percent);

      totalTimeMinutes /= work_percent;
      console.log(totalTimeMinutes);

      let completionTime = currentDate.getTime() + (totalTimeMinutes * 60 * 1000)
      let d = new Date(completionTime);

      this.date = `${d.toLocaleString('de',{timeZone:'Europe/Berlin', timeZoneName: 'long'})}`;
    },
  },
  created() {
    // Lade die Variablen beim Laden der Seite
    this.loadVariablesFromStorage();
  },
});
  
</script>
