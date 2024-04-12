# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
> 
> tokenB->tokenA->tokenD->tokenC->tokenB
> 
> 5 -> 5.655321988655322 -> 2.4587813170979333 -> 5.0889272933015155 -> 20.129888944077443

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
> 當交易規模較大或市場流動性較低時，買入或賣出資產的價格可能會因為訂單引起的市場價格變動而產生偏差，這種偏差就是滑點。
> 
> 其中最常見的是 $x*y=k$ 函數，也稱為恆定乘積模型。 這個函數確保了在交易時價格和交易規模之間存在一個固定的關係，從而降低了交易時的滑點。

```
function swap(uint256 amountIn, uint256 amountOutMin, address tokenIn, address tokenOut) external {

    // 根據 x * y = k 計算
    uint256 amountOut = (balances[tokenIn] * balances[tokenOut]) / (balances[tokenIn] + amountIn);
    require(amountOut >= amountOutMin, "Slippage too high");
}
```

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
> 
> mint 函數中，扣除初始流動性時會減去一定數量的最小流動性。 這個設計的目的是為了防止流動性提供者添加過小數量的流動性，從而導致價格異常波動或容易被攻擊。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
>
> 只能使用特定的公式來獲取流動性，這是為了確保流動性提供者根據其貢獻獲得公平的資產份額。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
>
> sandwich attack 是透過提前知道或乾預交易順序來從交易者身上獲利。
>
> 它可能會導致價格滑點增加、交易成本增加、交易執行延遲。

