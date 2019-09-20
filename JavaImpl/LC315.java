import java.util.*;

class LC315 {
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> result = new ArrayList<Integer> ();
        result.add(0);
        for(int start = nums.length -1; start > 0; start--){
            result.add(0, inSort(nums, start, nums[start - 1]));
        }
        return result;
    }
    
    //sort it in a descending way
    // start >= 1, index of target is start - 1
    private int inSort(int[] arr,int start, int target)
    {   if (start < 0)start = 0;
        int mid = 0, low = start, high = arr.length;
        while (low < high){
            mid = (low + high) / 2;
            if (arr[mid] == target){
                while (mid < arr.length - 1 && arr[mid + 1] == target) mid += 1;
                //now arr[mid] < target or mid = arr.length which is the index of target
                int k = start - 1;
                for (; k < mid; k ++){
                    arr[k] = arr[k+1];  //last round, k=mid-1, arr[mid-1] = arr[mid]
                } 
                arr[k] = target;//insert target:arr[mid] = target
                return mid - arr.length + 1;
            }
            else if (arr[mid] < target) high = mid;
            else if (arr[mid] > target) low = mid;
        }
     if (arr[start] < target)return arr.length - start;
     else if (arr[arr.length - 1] > target){
         int k = start - 1;
         for (; k < arr.length-1; k ++){
             arr[k] = arr[k+1];
         }
         arr[k] = target;//arr[length-1] = mid
         return 0;
     }
     return 0;
    }
}