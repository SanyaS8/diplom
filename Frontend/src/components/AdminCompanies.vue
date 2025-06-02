<script setup>

import ProfileTitle from "@/components/ProfileTitle.vue";
import {DataTable, Column, Button, Password, InputText} from "primevue";
import {ref} from "vue";
import Dialog from "primevue/dialog";

const visible = ref(false)
const company = ref({})

const users = ref([
  {
    id: 1,
    company: 'БЧ',
  },
  {
    id: 2,
    company: 'Грузоперевозки',
  },
  {
    id: 3,
    company: 'Аэрофлот',
  },
  {
    id: 4,
    company: 'БЧ',
  },
  {
    id: 5,
    company: 'Грузоперевозки',
  },
  {
    id: 6,
    company: 'Аэрофлот',
  },
  {
    id: 7,
    company: 'БЧ',
  },
  {
    id: 8,
    company: 'Грузоперевозки',
  },
  {
    id: 9,
    company: 'Аэрофлот',
  },
]);

function deleteUser(user) {
  users.value = users.value.filter(item => item.id !== user.id)
}
</script>

<template>
<div class="admin-races">
  <profile-title>
    <div class="title">
      Перевозчики
      <Button label="Создать" @click="visible = true" />
    </div>
  </profile-title>
  <div class="races-table">
    <DataTable :value="users" tableStyle="min-width: 100%">
      <Column field="id" header="ID"></Column>
      <Column field="company" header="Перевозчик"></Column>
      <Column class="w-24 !text-end">
        <template #body="{ data }">
          <Button icon="ri-delete-bin-6-line" @click="deleteUser(data)" severity="secondary" rounded></Button>
        </template>
      </Column>
    </DataTable>
  </div>

  <div class="card flex justify-center">
    <Dialog v-model:visible="visible" modal header="Создание перевозчика" :style="{ width: '25rem' }">
      <span style="display: block; margin-bottom: 40px">Укажите нужную информацию</span>
      <div style="display: flex; justify-content: space-between; align-items: center">
        <label for="name" style="font-weight: 600">Название</label>
        <InputText id="name" v-model="company.name" placeholder="Название компании" />
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
        <label for="login" style="font-weight: 600">Логин</label>
        <InputText id="login" v-model="company.login" placeholder="Логин компании" />
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
        <label for="password" style="font-weight: 600">Пароль</label>
        <Password id="password" v-model="company.password" placeholder="Пароль компании" />
      </div>
      <div style="margin-top: 30px; display: flex; gap: 10px;">
        <Button type="button" label="Отмена" severity="secondary" @click="visible = false"></Button>
        <Button type="button" label="Сохранить" @click="visible = false"></Button>
      </div>
    </Dialog>
  </div>
</div>
</template>

<style scoped>
.admin-races {
  width: 100%;
  margin-bottom: 50px;
}

.title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
</style>