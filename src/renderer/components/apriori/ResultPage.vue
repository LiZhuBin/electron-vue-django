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

    <el-table>
        <el-table
                :data="this.tableData"
                height="300"
                border
                style="width: 100%" >
            <el-table-column
                    v-for="{ prop, label } in colConfigs"
                    :key="prop"
                    :prop="prop"
                    :label="label">

            </el-table-column>

        </el-table>
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
        check : [],

      }
    },
    methods:{
      func:function () {
        //从store中获得选择的城市、日期、商品名称
        this.data.citiesSelect = [];
        this.data.dataSelect = this.$store.state.date_select;
        this.$store.state.goodsSelect = [];
        for (let city in this.$store.state.cities_select) {
          this.data.citiesSelect.push(this.$store.state.cities[city])
        }
        for (let good in this.$store.state.goods_select) {
          this.data.goodsSelect.push(this.$store.state.goods[good])
        }
      },
      run:function () {
        //this.$http.post('')
      }


    }
  }
</script>

<style scoped>

</style>