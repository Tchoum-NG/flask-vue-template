<template>
  <v-app>
    <v-app-bar
      color="blue lighten-2"
      dark
      dense
      app
    >
      <v-btn
        icon
        @click="switchdrawer"
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>
      <v-toolbar-title 
        class="pl-3" 
        color="white"
      >
        CookBook
      </v-toolbar-title>
    </v-app-bar>
  </v-app>
</template>

<script>

export default {

  methods:{
    switchdrawer() {
      this.$store.commit('switchSidebar');
    }
  }
}
</script>