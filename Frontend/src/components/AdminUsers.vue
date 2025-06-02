<script setup>

import ProfileTitle from "@/components/ProfileTitle.vue";
import { DataTable, Column, Button } from "primevue";
import {ref} from "vue";

const users = ref([
  {
    id: 1,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 2,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 3,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 4,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 5,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 6,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 7,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 8,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 9,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 10,
    name: 'Иванов Иван Иванович'
  },
  {
    id: 11,
    name: 'Иванов Иван Иванович'
  }
]);

function deleteUser(user) {
  users.value = users.value.filter(item => item.id !== user.id)
}
</script>

<template>
<div class="admin-users">
  <profile-title>Пользователи</profile-title>
  <div class="users-table">
    <DataTable :value="users" tableStyle="min-width: 100%">
      <Column field="id" header="ID"></Column>
      <Column field="name" header="Имя"></Column>
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
.admin-users {
  width: 100%;
}
</style>