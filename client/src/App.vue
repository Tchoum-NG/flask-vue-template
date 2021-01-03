<template>
  <v-app>
    <v-main>
      <Sidemenu />
      <Topbar />
      <RecipesList />
    </v-main>
  </v-app>
</template>

<script>
import Topbar from './components/Topbar.vue';
import Sidemenu from './components/Sidemenu.vue';
import RecipesList from './components/RecipesList.vue' 

export default {
  name: 'App',

  components: {
    Topbar,
    Sidemenu,
    RecipesList,
  },

  
};
</script>

<style>
html {
  overflow: hidden !important;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

html::-webkit-scrollbar {
  width: 0;
  height: 0;
}
</style>