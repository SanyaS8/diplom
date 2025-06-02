<script setup>

import ProfileTitle from "@/components/ProfileTitle.vue";
import { DataTable, Column, Button } from "primevue";
import {ref} from "vue";

const users = ref([
  {
    id: 143522,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 561231,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 123561,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 456212,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 345112,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 435123,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 873423,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 456231,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 457412,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 467231,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  },
  {
    id: 456721,
    name: 'Минск - Брест',
    cost: '10 000 р',
    company: 'БЧ',
    date: '10.10.2025'
  }
]);

function deleteUser(user) {
  users.value = users.value.filter(item => item.id !== user.id)
}
</script>

<template>
<div class="admin-races">
  <profile-title>Рейсы</profile-title>
  <div class="races-table">
    <DataTable :value="users" tableStyle="min-width: 100%">
      <Column field="id" header="ID"></Column>
      <Column field="name" header="Маршрут"></Column>
      <Column field="company" header="Перевозчик"></Column>
      <Column field="cost" header="Стоимость билета"></Column>
      <Column field="date" header="Дата"></Column>
      <Column class="w-24 !text-end">
        <template #body="{ data }">
          <Button icon="ri-delete-bin-6-line" @click="deleteUser(data)" severity="secondary" rounded></Button>
        </template>
      </Column>
    </DataTable>
  </div>
</div>
</template>

<style scoped>
.admin-races {
  width: 100%;
  margin-bottom: 50px;
}
</style>