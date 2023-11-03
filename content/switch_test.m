switch number_of_countries
    case 4
        msg='The answer is slightly higher';
    case 5
        msg='That is correct!';
    otherwise
        msg='Way off, try again';
end
disp(msg);
