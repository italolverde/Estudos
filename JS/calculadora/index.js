nums = []
ops = []
res = 0
display = document.getElementById('display')

function clicknum(num) {
    nums.push(num)
}

function clickop(op) {
    ops.push(op)
}

function calcular() {
    res = nums[0]
    for(i = 1; i<=nums.length; i++) {
        switch(ops[i-1]) {
            case 1:
                res += nums[i]
                break
            case 2:
                res -= nums[i]
                break
            case 3:
                res /= nums[i]
                break
            case 4:
                res *= nums[i]
                break
        }
    }
    console.log(res)
    console.log(nums.length)
    console.log(String(res))
    display.innerText = 'hiuhg'
