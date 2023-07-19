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
        label="Anzahl der Karten"
        type="number"
        filled
        class="menu__item"
      />
      <q-btn @click="updateTitleAndCards" class="menu__item">Einstellungen speichern</q-btn>
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

export default defineComponent({
  name: 'MangaPage',
  data() {
    return {
      pageTitle: 'Title', // Default-Titelseite
      numberOfCards: 0, // Standardanzahl von Karten
      cards: [],
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
          break;
        case 'card bubble':
          element.removeClass('bubble');
          element.toggleClass('fertig');
          break;
        case 'card raster':
          element.removeClass('raster');
          element.toggleClass('bubble');
          break;
        case 'card ink':
          element.removeClass('ink');
          element.toggleClass('raster');
          break;
        case 'card sketch':
          element.removeClass('sketch');
          element.toggleClass('ink');
          break;
        case 'card story':
          element.removeClass('story');
          element.toggleClass('sketch');
          break;
        case 'card nothing':
          element.removeClass('nothing');
          element.toggleClass('story');
          break;
        default:
          element.toggleClass('nothing');
          break;
      }
      this.cards[index] = element.attr('class').split(/\s+/)[1]
      localStorage.setItem('cards', JSON.stringify(this.cards)); // Speichere das cards-Array als JSON-String
      console.log(`Klassenname nachher: ${element.attr('class').split(/\s+/)[1]}`);
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

      // Speichere die Variablen im LocalStorage
      localStorage.setItem('pageTitle', this.pageTitle);
      localStorage.setItem('numberOfCards', this.numberOfCards.toString());
      localStorage.setItem('cards', JSON.stringify(this.cards)); // Speichere das cards-Array als JSON-String
    },
    loadVariablesFromStorage() {
      // Lade die Variablen vom LocalStorage, wenn sie vorhanden sind
      const storedPageTitle = localStorage.getItem('pageTitle');
      const storedNumberOfCards = localStorage.getItem('numberOfCards');
      const storedCards = localStorage.getItem('cards');

      if (storedPageTitle) {
        this.pageTitle = storedPageTitle;
      }

      if (storedNumberOfCards) {
        this.numberOfCards = parseInt(storedNumberOfCards, 10);
        this.cards = new Array(Number(storedNumberOfCards)).fill('nothing');
      }

      if (storedCards) {
        this.cards = JSON.parse(storedCards); // Wiederherstellen des cards-Arrays aus dem JSON-String
      }
    },
  },
  created() {
    // Lade die Variablen beim Laden der Seite
    this.loadVariablesFromStorage();
  },
});
  
</script>
