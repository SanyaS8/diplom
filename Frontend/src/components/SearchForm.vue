<script setup>
import {Card} from "primevue";
import {Select} from "primevue";
import {Button} from "primevue";
import {ref} from "vue";
import cities from "@/assets/cities.js";
import {DatePicker} from "primevue";

const selectedCity = ref(null);
const selectedCityTo = ref(null);
const start = ref(null)
const end = ref(null)
</script>

<template>
  <Card style="margin-top: 30px">
    <template #title>Путешествуйте к лучшему</template>
    <template #content>
      <form class="search">
        <Select v-model="selectedCity"
                :options="cities"
                optionLabel="city"
                placeholder="Откуда"
                class="w-full md:w-56"
                filter
                size="large"
        />
        <Select v-model="selectedCityTo"
                :options="cities"
                optionLabel="city"
                placeholder="Куда"
                class="w-full md:w-56"
                filter
                size="large"
        />
        <DatePicker v-model="start" placeholder="Когда" dateFormat="dd.mm.yy" />
        <DatePicker v-model="end" placeholder="Обратно" dateFormat="dd.mm.yy" />
        <Button label="Найти билеты" />
      </form>
    </template>
  </Card>
</template>

<style scoped>
.search {
  display: flex;
  gap: 10px;
}

.search .p-component {
  width: 100%;
}
</style>