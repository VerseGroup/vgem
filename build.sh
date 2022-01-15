rmdir -rf build
rmdir -rf dist

cd src
rmdir -rf vg_em.egg-info

cd ..

python3 setup.py sdist bdist_wheel