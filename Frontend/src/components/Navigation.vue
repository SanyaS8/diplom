<script setup>
import {Menubar} from "primevue";
import {Button} from "primevue";
import {computed, ref} from "vue";
import {useRouter} from "vue-router";
import { useStore } from "vuex";

const router = useRouter()
const store = useStore()

const user = computed(() => {
  return store.state.auth.user;
})

const items = ref([
  {
    label: 'Все',
    icon: 'ri-coupon-3-line'
  },
  {
    label: 'Поезда',
    icon: 'ri-train-line'
  },
  {
    label: 'Самолеты',
    icon: 'ri-flight-takeoff-line'
  }
]);
</script>

<template>
  <div class="card">
    <Menubar :model="items">
      <template #start>
        <div class="logo" @click="router.push('/')">
          Marshrut.BY
          <img src="/flower.png" alt="" style="width: 30px">
        </div>
      </template>
      <template #end>
        <Button @click="router.push('/profile')" label="Профиль" rounded icon="ri-login-circle-line" v-if="user" />
        <Button @click="router.push('/login')" label="Войти" rounded icon="ri-login-circle-line" v-else />
      </template>
    </Menubar>
  </div>
</template>

<style>
.logo {
  font-size: 20px;
  font-weight: 600;
  letter-spacing: 2px;
  cursor: pointer;
  transition: ease-in-out 0.2s;

  display: flex;
  gap: 5px;
  align-items: center;


  &:hover {
    opacity: 0.8;
  }
}


.logo img {
  margin-bottom: 3px;
}

.p-menubar {
  background-color: #6265c6 !important;
  color: #fff !important;
}

.p-menubar-item-icon {
  color: #fff !important;
}
.p-menubar-item-link {
  color: #fff !important;
}

.p-menubar-item-content:hover {
  background-color: #9091ea !important;
}
</style>