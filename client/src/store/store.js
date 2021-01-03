import Vue from 'vue';
import Vuex from 'vuex';
import MainNavigationDrawer from './modules/MainNavigationDrawer';

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    MainNavigationDrawer: MainNavigationDrawer
  }
});