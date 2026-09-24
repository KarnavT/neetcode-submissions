class Solution {
    public void sortColors(int[] nums) {
        int r = 0;
        int w = 0;
        int b = 0;

        for(int num : nums) {
            if (num == 0) {
                r++;
            } else if (num == 1) {
                w++;
            } else {
                b++;
            }
        }
        int[] merge = new int[r + w + b];

        int idx = 0;
        for (int i = 0; i < r; i++) nums[idx++] = 0;
        for (int i = 0; i < w; i++) nums[idx++] = 1;
        for (int i = 0; i < b; i++) nums[idx++] = 2;
    }
}