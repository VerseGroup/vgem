rmdir build
rmdir dist

cd src
rmdir vg_em.egg-info

cd ..

python3 setup.py sdist bdist_wheel