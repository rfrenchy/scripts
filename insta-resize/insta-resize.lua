

-- object for creating a square image for instagram
local square = {
    -- return a 1:1 dimension string of image
    dimension = function (height, width)
        -- use whatever measurement is biggest  
        local d = height > width and height or width;
        -- create 1:1 string of biggest measurement e.g. 1230x1230
        return d
    end,

    -- return instagram specific 1:1 measurement 
    instasize = function () return "1080x1080" end
}

-- object for creating portrait sized images for instagram
local portrait = {
    -- return a 4:5 dimension string of image
    dimension = function (height, width)   
        local wx = (height / 5) * 4 -- new width
        return string.gsub("%sx" .. height, "%s", wx)
    end,
    -- return instagram specific portrait size 
    instasize = function () return "1080x1350" end
}

local landscape = {
    dimension = function () return "" end,
    instasize = function () return "" end
}

print(square.dimension(200, 199))

-- print(main[arg[1]])