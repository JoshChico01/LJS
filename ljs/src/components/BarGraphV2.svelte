<script>

    export let ages

    



    // Populate the bin_dict with ages
    function getData(ages) {
        let bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
        let bin_dict = { "0-10": [] };

        // Create bins dynamically
        for (let i = 0; i < bins.length - 1; i++) {
            bin_dict[(bins[i] + 1) + "-" + bins[i + 1]] = [];
        }
        bin_dict["100+"] = [];
    
        for (let age of ages) {
            if (age <= 10) {
                bin_dict["0-10"].push(age);
            } else if (age > 100) {
                bin_dict["100+"].push(age);
            } else {
                for (let i = 0; i < bins.length - 1; i++) {
                    if (age > bins[i] && age <= bins[i + 1]) {
                        bin_dict[(bins[i] + 1) + "-" + bins[i + 1]].push(age);
                        break;
                    }
                }
            }
        }

        let bin_keys = Object.keys(bin_dict)
        let data = []

        for (let key of bin_keys){
            data.push({ label: key, value: bin_dict[key].length })
        }

        return data
    }

    $: data = getData(ages)
    $: maxValue = Math.max(...data.map(d => d.value))  * 1.5;

    
  </script>
  
  <style>
    .bar-container {
      display: flex;
      align-items: flex-end;
      height: 200px;
      width: 100%;
      margin-top: 20px;
      border-left: 1px solid black;
    }
  
    .bar {
      width: 40px;
      margin-left: 30px;
      background-color: #3490dc;
      text-align: center;
      color: white;
      text-align: center;
    }
  
    .label {
      margin-top: 10px;
      text-align: center;
    }

    .value {
      text-align: center;
        
    }

    .hr{
        width: 100%;
        height: 1px;
        background-color: black;
    }
  </style>
  
  <div class="bar-container">
    {#each data as { label, value }}
      <div style="width:100px">
        <div class="bar" style="height: {200 * (value / maxValue)}px"></div>
        <div class="hr"></div>
        <div class="value">{value}</div>
        <div class="label">{label}</div>
      </div>
    {/each}
  </div>
  