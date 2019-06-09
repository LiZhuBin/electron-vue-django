<template>
    <div>
        <div style="text-align:center" slot="header">
            <el-button type="primary" round @click="func">数据切片查询</el-button>

        </div>
<div>
        <el-tag
                v-for="tag in data.citiesSelect"
                closable
                >
            {{tag}}
        </el-tag>
</div>
        <div>
        <el-tag
                v-for="tag in data.dataSelect"
                closable
        >
            {{tag}}
        </el-tag>
        </div>
        <div>
        <el-tag
                v-for="tag in data.goodsSelect"
                closable
        >
            {{tag}}
        </el-tag>
        </div>
<div>{{this.result}}</div>
        <el-table
                :data="result"
                style="width: 100%">
            <el-table-column
                    prop="date"
                    label="日期"
                    width="150">
            </el-table-column>
            <div v-for="city in data.citiesSelect">
            <el-table-column label=city >
                <el-table-column label= "广东省" >

                    <el-table-column
                            prop="data"
                            label=good
                            width="120">
                    </el-table-column>

                    </el-table-column>

            </el-table-column>
            </div>
        </el-table>
    </div>
</template>

<script>
  export default {
    name: "ResultPage",
    data(){
      return{
        data:{
          'citiesSelect':[],
        'dataSelect':[],
        'goodsSelect':[]},
        result :[],
        check : [],


      }
    },
    methods:{
      func:function () {
        //从store中获得选择的城市、日期、商品名称
        this.data.citiesSelect = [];
        this.data.dataSelect = this.$store.state.date_select;
        this.data.goodsSelect = [];

        for (let city in this.$store.state.cities_select) {
          this.data.citiesSelect.push(this.$store.state.cities[city])
        }
        for (let good in this.$store.state.goods_select) {
          this.data.goodsSelect.push(this.$store.state.goods[good])
        }
        console.info(this.data);
        this.run()
      },
      run:function () {
        this.$http.get('data-change/anaylse',{
          params:{
                selectData : this.data
          }}).then((res)=>{
            this.result = res.data
            console.log(res)
        })
      }


    }
  }
</script>

<style scoped>

</style>