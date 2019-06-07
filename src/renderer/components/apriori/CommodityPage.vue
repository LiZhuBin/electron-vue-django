<template>
    <el-card >
        <el-header>选择地区</el-header>
        <el-main>
            <el-transfer
                    filterable
                    :filter-method="filterMethod"
                    filter-placeholder="请输入城市拼音"
                    v-model="value"
                    :titles="['商品集', '选择商品']"
                    :data="data"
                    @change="handleChange">
            </el-transfer>
        </el-main>
    </el-card>

</template>

<script>
  export default {

    name: "Commodity",

    data() {
      const generateData = _ => {
        const data = [];
        const commodities = ['面包','奶类','零食','酒类','方便面','水果'];
        commodities.forEach((city, index) => {
          data.push({
            label: city,
            key: index,
            commodity: commodities[index]
          });
        });
        return data;
      };
      return {
        data: generateData(),
        value: [],
        filterMethod(query, item) {
          return item.commodity.indexOf(query) > -1;
        }
      };
    },
    methods:{
      handleChange(value, direction, movedKeys) {

        this.$store.state.goods_select = value
      },
    }
  }
</script>

<style scoped>

</style>