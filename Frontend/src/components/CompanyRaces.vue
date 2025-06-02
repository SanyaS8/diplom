<script setup>

import ProfileTitle from "@/components/ProfileTitle.vue";
import {DataTable, Column, Button, Password, InputText, DatePicker, Select} from "primevue";
import {ref} from "vue";
import Dialog from "primevue/dialog";
import cities from "@/assets/cities.js";

const race = ref({})
const visible = ref(false)

const users = ref([
  {
    id: 143522,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '10/124',
    date: '10.10.2025'
  },
  {
    id: 561231,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '10/124',
    date: '10.10.2025'
  },
  {
    id: 123561,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '10/124',
    date: '10.10.2025'
  },
  {
    id: 456212,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '15/124',
    date: '10.10.2025'
  },
  {
    id: 345112,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '41/124',
    date: '10.10.2025'
  },
  {
    id: 435123,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '54/124',
    date: '10.10.2025'
  },
  {
    id: 873423,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '23/124',
    date: '10.10.2025'
  },
  {
    id: 456231,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '76/124',
    date: '10.10.2025'
  },
  {
    id: 457412,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '11/124',
    date: '10.10.2025'
  },
  {
    id: 467231,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '43/124',
    date: '10.10.2025'
  },
  {
    id: 456721,
    name: 'Минск - Брест',
    cost: '10 000 р',
    amount: '23/124',
    date: '10.10.2025'
  }
]);

function deleteUser(user) {
  users.value = users.value.filter(item => item.id !== user.id)
}

function cancel(user) {
  user.cancel = true
}
function edit(user) {
  visible.value = true
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
      <Column field="name" header="Маршрут"></Column>
      <Column field="cost" header="Стоимость билета"></Column>
      <Column field="amount" header="Количествуо билетов"></Column>
      <Column field="date" header="Дата"></Column>
      <Column class="w-24 !text-end">
        <template #body="{ data }">
          <div class="buttons">
            <Button icon="ri-pencil-line" @click="edit(data)" severity="success" rounded size="small"></Button>
            <Button icon="ri-close-line" @click="cancel(data)" severity="warn" rounded size="small"></Button>
            <Button icon="ri-delete-bin-6-line" @click="deleteUser(data)" severity="danger" rounded size="small"></Button>
          </div>
        </template>
      </Column>
    </DataTable>
  </div>

  <div class="card flex justify-center">
    <Dialog v-model:visible="visible" modal header="Рейс" :style="{ width: '25rem' }">
      <span style="display: block; margin-bottom: 40px">Укажите нужную информацию</span>
      <div style="display: flex; justify-content: space-between; align-items: center">
        <label for="id" style="font-weight: 600">Номер рейса</label>
        <InputText id="id" v-model="race.name" placeholder="Номер рейса" />
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
        <label for="date" style="font-weight: 600">Дата</label>
        <DatePicker format="dd.mm.yy" v-model="race.date" />
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
        <label for="from" style="font-weight: 600">Откуда</label>
        <Select v-model="race.from"
                style="width: 200px"
                :options="cities"
                optionLabel="city"
                placeholder="Откуда"
                filter
        />
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
        <label for="to" style="font-weight: 600">Куда</label>
        <Select v-model="race.to"
                style="width: 200px"
                :options="cities"
                optionLabel="city"
                placeholder="Куда"
                filter
        />
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

.buttons {
  display: flex;
  gap: 10px;
}

.title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
</style>