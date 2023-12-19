#### Derivation of L'Hôpital's Rule
$$
\lim_{x\to a}\frac{f(x)}{g(x)}:f(a)=g(a)=0
$$
$$
\lim_{x\to a}\frac{f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3 + \cdots}{g(a) + g'(a)(x - a) + \frac{g''(a)}{2!}(x - a)^2 + \frac{g'''(a)}{3!}(x - a)^3 + \cdots}
$$
$$
=\lim_{x\to a}\frac{f'(a)(x - a) + \frac{f''(a)}{2}(x - a)^2 + \cdots}{g'(a)(x - a) + \frac{g''(a)}{2}(x - a)^2 + \cdots}\quad\because f(a)=g(a)=0
$$
$$
=\lim_{x\to a}\frac{f'(a) + \frac{f''(a)}{2}(x - a) + \cdots}{g'(a) + \frac{g''(a)}{2}(x - a) + \cdots}\quad\text{by dividing through by }(x-a)
$$
$$
=\lim_{x\to a}\frac{f'(a)}{g'(a)}\quad\because \lim_{x\to a}(x-a)=0
$$
