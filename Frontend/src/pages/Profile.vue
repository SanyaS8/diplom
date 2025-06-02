<script setup>
import Navigation from "@/components/Navigation.vue";

import {Menu} from "primevue";
import {ref} from "vue";
import ProfileTickets from "@/components/ProfileTickets.vue";
import ProfileCards from "@/components/ProfileCards.vue";
import ProfileLogout from "@/components/ProfileLogout.vue";
import {useStore} from "vuex";
import AdminUsers from "@/components/AdminUsers.vue";
import AdminRaces from "@/components/AdminRaces.vue";
import AdminCompanies from "@/components/AdminCompanies.vue";
import CompanyInfo from "@/components/CompanyInfo.vue";
import CompanyRaces from "@/components/CompanyRaces.vue";

const store = useStore()
const selectMenu = ref('profile')

const items = ref([
  {
    label: 'Аккаунт',
    items: [
      {
        label: 'Профили',
        icon: 'ri-profile-line',
        id: 'profile'
      },
      {
        label: 'Билеты',
        icon: 'ri-coupon-line',
        id: 'ticket'
      },
      {
        label: 'Выход',
        icon: 'ri-logout-box-r-line'
      }
    ]
  },
]);

if (store.state.auth.role === 2) {
  items.value.push({
    label: 'Администратор',
    items: [
      {
        label: 'Пользователи',
        icon: 'ri-group-line',
        id: 'users'
      },
      {
        label: 'Рейсы',
        icon: 'ri-route-line',
        id: 'races'
      },
      {
        label: 'Перевозчики',
        icon: 'ri-building-line',
        id: 'transport'
      }
    ]
  });
} else

if (store.state.auth.role === 3) {
  items.value.push({
    label: 'Перевозчик',
    items: [
      {
        label: 'Информация',
        icon: 'ri-information-line',
        id: 'info'
      },
      {
        label: 'Рейсы',
        icon: 'ri-route-line',
        id: 'company-races'
      },
    ]
  });
}
</script>

<template>
  <navigation />
  <div class="profiles">
    <div class="card flex justify-center">
      <Menu :model="items">
        <template #item="{ item, props }">
          <div class="menu-item" :class="{ active: selectMenu === item.id }" @click="selectMenu = item.id">
            <i :class="item.icon"></i>
            {{ item.label }}
          </div>
        </template>
      </Menu>
    </div>

    <profile-cards v-if="selectMenu === 'profile'" />
    <profile-tickets v-else-if="selectMenu === 'ticket'" />
    <admin-users v-else-if="selectMenu === 'users'" />
    <admin-races v-else-if="selectMenu === 'races'" />
    <admin-companies v-else-if="selectMenu === 'transport'" />
    <company-info v-else-if="selectMenu === 'info'" />
    <company-races v-else-if="selectMenu === 'company-races'" />
    <profile-logout v-else />
  </div>
</template>

<style scoped>
.menu-item {
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 15px;
}

.menu-item.active {
  background-color: var(--p-button-primary-background);
  color: #fff;
}

.profiles {
  display: flex;
  margin-top: 50px;
  gap: 50px;
}

.create-profile {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100px;
}
</style>