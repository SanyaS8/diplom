import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { ru } from 'primelocale/js/ru.js'
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import 'remixicon/fonts/remixicon.css';
import store from './store'

const app = createApp(App)

app.use(router)

app.use(PrimeVue, {
    locale: ru,
    theme: {
        preset: Aura,
        options: {
            darkModeSelector: false,
        }
    },
})

app.use(store)

app.mount('#app')
