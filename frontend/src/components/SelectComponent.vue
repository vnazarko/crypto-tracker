<script lang="ts" setup>
import axios from 'axios';

function getCryptocurrencies() {
    axios.get(`https://${import.meta.env.VITE_API_URL}/crypto/get`)
    .then((response) => {
        console.log(response.data);
        
        return response.data.payload;
     })
}
</script>
<template>
    <div class="container">
        <nav class="select-coin">
            <label 
                v-for="(coin, index) in getCryptocurrencies()"
                :key="index"
                :for="coin.name" 
                class="select-coin_label label"
            >
                <input 
                    type="radio" 
                    name="coin" 
                    :id="coin.name" 
                    class="select-coin_item select-item"
                >
                {{ coin.name }}
            </label>
            
        </nav>
    </div>
</template>

<style lang="sass" scoped>

</style>