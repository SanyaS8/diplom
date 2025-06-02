<script setup>
import Navigation from "@/components/Navigation.vue";
import SearchForm from "@/components/SearchForm.vue";
import TicketList from "@/components/TicketList.vue";
</script>

<template>
  <div class="main-page">
    <navigation />
    <search-form />
    <ticket-list />
  </div>
</template>

<style>
.main-page {
  padding-bottom: 50px;
}
</style>