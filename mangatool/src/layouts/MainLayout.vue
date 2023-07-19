<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> Mangatool </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> Menu </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
      <q-tabs >
        <q-route-tab to="/manga" name="manga">Go to</q-route-tab>
      </q-tabs> 
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";

const linksList = [
  {
    title: "Dashboard",
    caption: "Alle Werte zu den Mangas",
    icon: "analytics",
    link: "/",
  },
  {
    title: "Manga 1",
    caption: "github.com/quasarframework",
    icon: "menu_book",
    link: "/manga/manga",
  },
  {
    title: "Manga 2",
    caption: "chat.quasar.dev",
    icon: "menu_book",
    link: "/manga/manga",
  },
  {
    title: "Manga 3",
    caption: "forum.quasar.dev",
    icon: "menu_book",
    link: "/manga/manga",
  },
  {
    title: "Manga 4",
    caption: "@quasarframework",
    icon: "menu_book",
    link: "/manga/manga",
  },
  {
    title: "Manga hinzufügen",
    caption: "",
    icon: "add",
    link: "/manga/manga",
  },
  {
    title: "Erschaffen von Leon Wempe",
    caption: "Link zur Website",
    icon: "brush",
    link: "https://leonwempe.com",
  },
];

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
