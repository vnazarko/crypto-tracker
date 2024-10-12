<script setup>
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';

let coins = ref([]);
let currencies = [
    'RUB', 'USD'
];
let stockMarkets = [
    'Binance', 'OKX', 'BYBIT'
]

let selectedCoin = ref(1);
let selectedCurrency = ref('RUB');
let selectedStockMarket = ref('Binance');

watch(selectedCoin, () => {
    localStorage.setItem('coin', selectedCoin.value);
})
watch(selectedCurrency, () => {
    localStorage.setItem('currency', selectedCurrency.value);
})
watch(selectedStockMarket, () => {
    localStorage.setItem('stock-market', selectedStockMarket.value);
})

async function getCryptocurrencies() {
    try {
        let res = await axios.get(`${import.meta.env.VITE_API_URL}/crypto/get`, {
            headers: {
                'Content-Type': 'application/json',
            },
        });
        coins.value = res.data.payload;    
    } catch (error) {
        console.error("Ошибка при получении монет", error);
    }
}
 
onMounted(() => {
    getCryptocurrencies();    
});


</script>
<template>
    <div class="container">
        <nav class="select-coin">
            <form id="coin" class="select-container">
                <div class="select-wrapper"
                    v-for="coin in coins"
                    :key="coin.coin_id"
                >
                    <input 
                        type="radio" 
                        name="coin" 
                        :id="coin.name" 
                        v-model="selectedCoin"
                        :value="coin.coin_id"
                        class="select-coin_label_item label_select-item"
                    >
                    <label :for="coin.name" class="select-coin_label label">
                        <p class="label_select-item_text">{{ coin.name }}</p>
                    </label>
                </div>
            </form>
        </nav>

        <div class="bottom">
            <nav class="bottom_select-currency">
                <form id="currency" class="select-container">
                    <div class="select-wrapper"
                        v-for="(currency, index) in currencies"
                        :key="index"
                    >
                        <input 
                            type="radio" 
                            name="coin" 
                            :id="currency" 
                            v-model="selectedCurrency"
                            :value="currency"
                            class="bottom_select-currency_label_item label_select-item"
                        >
                        <label :for="currency" class="bottom_select-currency_label label">
                            <p class="label_select-item_text">{{ currency }}</p>
                        </label>
                    </div>
                </form>
            </nav>

            <nav class="bottom_select-stock-market">
                <form id="stock-market" class="select-container">
                    <div class="select-wrapper"
                        v-for="(stockMarket, index) in stockMarkets"
                        :key="index"
                    >
                        <input 
                            type="radio" 
                            name="coin" 
                            :id="stockMarket" 
                            v-model="selectedStockMarket"
                            :value="stockMarket"
                            class="bottom_select-stock-market_label_item label_select-item"
                        >
                        <label :for="stockMarket" class="bottom_select-stock-market_label label">
                            <p class="label_select-item_text">{{ stockMarket }}</p>
                        </label>
                    </div>
                </form>
            </nav>
        </div>
    </div>
</template>

<style lang="sass" scoped>
.select-coin 
    width: 100%
    height: 40px
    margin-top: 60px
    .select-container 
        height: 100%
        width: 100%
        display: grid
        grid-template-columns: repeat(3, auto)

.bottom 
    width: 100%
    margin-top: 25px
    display: flex 
    justify-content: space-between
    gap: 20px
    &_select-currency
        height: 40px
        max-width: 246px
        min-width: 160px
        width: 100%
        .select-container 
            width: 100%
            height: 100%
            display: grid
            grid-template-columns: repeat(2, auto)
    &_select-stock-market
        height: 40px
        max-width: 873px
        min-width: 400px
        width: 100%
        .select-container 
            width: 100%
            height: 100%
            display: grid
            grid-template-columns: repeat(3, auto)

.select-container
    background-color: #0F172A
    border-radius: 8px
    padding: 4px

.label 
    width: 100%
    height: 100%
    display: flex
    justify-content: center 
    align-items: center
    cursor: pointer
    transition: all .3s
    border-radius: 6px
    &_select-item:checked + &
        background-color: #030712 
    &_select-item 
        appearance: none
        display: none
        &_text
            font-family: DM_Sans
            font-weight: 500 
            font-size: 14px
            color: #EFFDF5

@media (max-width:630px) 
    .bottom 
        flex-direction: column
        gap: 10px
        &_select-currency 
            max-width: 100%
        &_select-stock-market
            max-width: 100%
            min-width: 0
</style>