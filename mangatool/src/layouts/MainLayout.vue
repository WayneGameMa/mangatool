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
    link: "https://quasar.dev",
  },
  {
    title: "Manga 1",
    caption: "github.com/quasarframework",
    icon: "menu_book",
    link: "https://github.com/quasarframework",
  },
  {
    title: "Manga 2",
    caption: "chat.quasar.dev",
    icon: "menu_book",
    link: "https://chat.quasar.dev",
  },
  {
    title: "Manga 3",
    caption: "forum.quasar.dev",
    icon: "menu_book",
    link: "https://forum.quasar.dev",
  },
  {
    title: "Manga 4",
    caption: "@quasarframework",
    icon: "menu_book",
    link: "https://twitter.quasar.dev",
  },
  {
    title: "Manga hinzufügen",
    caption: "",
    icon: "add",
    link: "https://facebook.quasar.dev",
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
