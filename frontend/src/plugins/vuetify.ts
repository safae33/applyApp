import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import tr from 'vuetify/src/locale/tr';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
        primary: '#5244ee',
        secondary: '#424242',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107',
        myColor: '#363062',
        headerColor: '#827397',
        listColor: '#1e1d29'
      },
    },
  },
  lang: {
    locales: { tr },
    current: 'tr',
  },
});
